"""
Question handler for the app.
Contains 1 class:
* QuestionHandler

Parses a query and returns

Quentin Lathiere - synkx@hotmail.fr
"""

import os
import re
import json

from unidecode import unidecode
from urllib.parse import quote

from gpb_app.utils.utils import GMapsRequest
from gpb_app.utils.utils import MediaWikiRequest
from gpb_app.views import app

import logging

logger = logging.getLogger()


class QuestionHandler:

    JSON_OK = 'OK'
    """ Used by the JSON output to inform that everything has been found """
    JSON_GEOLOC_ONLY = 'GEOLOC_ONLY'
    """ Used by the JSON output to inform that only the geolocation info were found """
    JSON_NOTHING = 'NOTHING_FOUND'
    """ Used by the JSON output to inform that nothing has been found """

    def __init__(self, user_query):
        self.user_query = user_query
        self.output = False

        self.parse()

    def parse(self):
        """
        Parses a query (question from user).
        Filters unnecessary words via some provided filters.
        see /data folder.
        :rtype: str
        """

        # list of stop words in user language
        stop_words = "stop_words_{}.json".format(app.config["LANG"])
        stop_words = os.path.join('gpb_app/data', stop_words)

        # list of half words in user language
        half_words = "half_words_{}.json".format(app.config["LANG"])
        half_words = os.path.join('gpb_app/data', half_words)

        # open filter file and convert json to python object
        with open(half_words, 'r', encoding="utf-8") as half_words_filter:
            half_words_filter = json.load(half_words_filter)

        with open(stop_words, 'r', encoding="utf-8") as query_filter:
            query_filter = json.load(query_filter)

        # remove half words and diacritics
        query = unidecode(self.user_query)
        for half_word in half_words_filter:
            query = query.replace(half_word, '')

        # remove punctuation
        query = re.sub(r"[\!\,\.\?\"\'\<\>\[\]\~\`\\\/\=\&]+", "", query)
        query = query.split()

        self.user_query = " ".join(
            [w.lower() for w in query if w.lower() not in query_filter])

        # the query with half words and stop words removed
        return self.user_query

    def to_output(self):
        """
        Converts all required API datas to a json, then to a str
        via json.dumps() method.
        :rtype: str or False
        """
        if self.output:
            return self.output

        # empty output init
        self.output = {
            "query": self.user_query,
            "status": self.JSON_NOTHING,
            "address": "",
            "lat": "",
            "lng": "",
            "title": "",
            "url": "",
            "extract": "",
            "iframe_map": ""
        }

        # if self.user_query is False
        if not self.user_query:
            return self.output

        # Get data from Google Maps
        geoloc_req = GMapsRequest(self.user_query).filter_data()

        # if geoloc_req is False
        if not geoloc_req:
            return self.output

        self.output['address'] = geoloc_req.address
        self.output['lat'] = geoloc_req.lat
        self.output['lng'] = geoloc_req.lng
        self.output['status'] = self.JSON_GEOLOC_ONLY   # update status

        encoded_address = quote(self.output['address'])

        iframe = """
                <iframe
                    width="100%"
                    height="350"
                    frameborder="0"
                    style="border:0"
                    src=
                    'https://www.google.com/maps/embed/v1/place?q={}&key={}'
                    allowfullscreen>
                </iframe>
                """.format(
            encoded_address, app.config['GMAPS_GEOCODING_API_KEY'])

        self.output['iframe_map'] = iframe

        # Get data from WikiMedia
        mediawiki_req = MediaWikiRequest(
            geoloc_req.lat, geoloc_req.lng).get_data()

        # if mediawiki_req is False
        if not mediawiki_req:
            return self.output

        self.output['title'] = mediawiki_req.title
        self.output['extract'] = mediawiki_req.extract
        self.output['url'] = mediawiki_req.url
        self.output['status'] = self.JSON_OK  # update status

        # Prepare ready-to-embed Google Map's iframe with the address query
        encoded_address = quote(self.output['address'])

        # Encoding and return
        return self.output
