import json
from unidecode import unidecode

from random import randint

from urllib.request import urlopen

from gpb_app.views import app

import logging

logger = logging.getLogger()


class GMapsRequest:
    """
    Custom class:
    Handling Google Maps API requests
    """

    def __init__(self, address_query, auto_search=False):
        self.data_response = False
        self.data = False

        self.url = app.config["GMAPS_GEOCODING_API_URL"]
        self.api_key = app.config["GMAPS_GEOCODING_API_KEY"]
        self.address_query = address_query

        if auto_search:
            self.search()

    def search(self):
        """
        Sends a cleaned address query to gmaps API.
        Returns the json dump from the gmaps API response, or False.
        :rtype: False or json data
        """
        self.data_response = False

        self.address_query = unidecode(self.address_query).lower().split()
        self.address_query = "+".join(self.address_query)

        # builds the final url to request
        gmaps_url = self.url
        gmaps_url += ("address=" + self.address_query)
        gmaps_url += "&key="
        gmaps_url += self.api_key

        try:
            # use requests module to get the respons from the passed url
            json_response = urlopen(gmaps_url)
            json_response = json.loads(json_response.read().decode('utf8'))

        except Exception as traceError:
            traceError = 'GoogleMaps API request error:\n{}'.format(traceError)
            logger.warning(traceError)
            return False

        # if 'status' exists and is set to 'OK', then return the json,
        # and set self.data_response to the json_response var, in order
        # to access it from another function
        if 'status' in json_response.keys() \
                and json_response['status'] == "OK":
            self.data_response = json_response
            return json_response
        else:
            self.data_response = False
            return False

    def filter_data(self):
        """
        Filters data from gmaps json response
        :rtype: str
        """
        # Data response available ?
        if not self.data_response:
            if not self.search():  # if not: search
                return False  # if no result, return False

        if not self.data:
            try:
                gmaps_raw_data = self.data_response['results'][0]
                gmaps_filtered_data = {
                    "address": gmaps_raw_data['formatted_address'],
                    "lat": gmaps_raw_data['geometry']['location']['lat'],
                    "lng": gmaps_raw_data['geometry']['location']['lng'],
                    "place_id": gmaps_raw_data['place_id'],
                }
                self.data = GoogleMapsData(**gmaps_filtered_data)

            except Exception as traceError:
                traceError = (
                    "Google Maps API error while preparing search data "
                    "for \"{}\":\n Original message: {}".format(
                        self.address_query, traceError))
                logger.warning(traceError)
                return False

        return self.data


class GoogleMapsData:
    def __init__(self, address, lat, lng, place_id):
        self.address = address
        self.lat = lat
        self.lng = lng
        self.place_id = place_id

    def __str__(self):
        attributes = {
            "address": self.address,
            "lat": self.lat,
            "lng": self.lng,
            "place_id": self.place_id
        }

        return str(attributes)


class MediaWikiRequest:
    """
    Custom class:
    Handling MediaWiki API requests
    """

    def __init__(self, lat, lng, auto_search=False, random_place=None):
        self.bound_places_data = False
        self.extracts_data = False
        self.lat = lat
        self.lng = lng
        self.mediawiki_url = app.config["MEDIAWIKI_API_URL"]
        self.data = False  # Final data set, MediaWikiData object
        self.random_place = random_place

        if auto_search:
            self.search()

    def search(self):
        """ method wrapper """
        self.geo_search()
        self.get_extracts()

    def geo_search(self):
        """
        Builds an url based on the passed lat and lng
        :rtype: dict or False (bool)
        """

        self.bound_places_data = False
        self.extracts_data = False

        mediawiki_url = self.mediawiki_url
        mediawiki_url += "query&list=geosearch&gsradius=1000"
        mediawiki_url += ('&gscoord=' + str(self.lat) + '|' + str(self.lng))
        mediawiki_url += "&format=json"

        try:
            json_response = urlopen(mediawiki_url)
            json_response = json.loads(json_response.read().decode('utf8'))

        except Exception as traceError:
            traceError = 'Mediawiki: geosearch API request error:\n{}'.format(
                traceError)
            logger.error(traceError)
            return False

        if 'query' in json_response.keys():
            self.bound_places_data = json_response
            return json_response
        else:
            self.bound_places_data = False
            return False

    def get_extracts(self):
        """
        :rtype: dict or False (bool)
        """

        page_id = 0

        try:
            if self.random_place is None:
                # chose a random place for the places around the given address
                self.random_place = randint(0, len(
                    self.bound_places_data['query']['geosearch']) - 1)
            else:
                self.random_place

            page_id = (
                self.bound_places_data['query']['geosearch'][
                    self.random_place]['pageid'])

            # return mediawiki infos about a place

        except Exception as trace:
            trace = ("mediawiki API error while preparing search data "
                     "for \"{}|{}\":\n{}".format(self.lat, self.lng, trace))
            app.logger.info(trace)
            return False

        # reset self.extracts_data
        self.extracts_data = False

        # build the mediawiki url to get the article intro about the place
        mediawiki_article_url = self.mediawiki_url
        mediawiki_article_url += "query&pageids="
        mediawiki_article_url += str(page_id)
        mediawiki_article_url += "&prop=extracts"
        mediawiki_article_url += "&exintro"
        mediawiki_article_url += "&format=json"

        try:
            json_response = urlopen(mediawiki_article_url)
            json_response = json.loads(json_response.read().decode('utf8'))

        except Exception as trace:
            trace = 'Mediawiki extracts API request error:\n{}, {}'.format(
                trace, mediawiki_article_url)
            app.logger.error(trace)
            return False

        if ('query' in json_response.keys() and
                'missing' not in
                json_response['query']['pages'][str(page_id)].keys()):
            self.extracts_data = json_response

        return self.extracts_data

    def get_data(self):
        """
        Returns the content of the search in a MediaWikiData object
        Launches the search if needed.
        The result is also stored in self.data.
        :rtype: MediaWikiData custom object or False
        """
        #
        # Do we have data ?
        #
        # Launches geo_search
        # and get_extracts if nothing has been loaded
        if not self.bound_places_data:
            if self.geo_search():
                self.get_extracts()

        # If we get there, we are sure the search has been done
        # but returned nothing
        # If self.extracts_data is False:
        if not self.extracts_data:
            return False

        #
        # Data structure
        #
        if not self.data:
            # We need the pageid of the article fetched from geosearch data
            page_id = self.bound_places_data['query']['geosearch'][
                self.random_place]['pageid']
            results = self.extracts_data['query']['pages'][str(page_id)]

            filtered_data = {
                "title": results['title'],
                "pageid": results['pageid'],
                "url": "https://{}.wikipedia.org/?curid={}",
                "extract": results['extract']
            }

            # Url
            filtered_data['url'] = filtered_data['url'].format(
                app.config['LANG'], page_id)

            # Instanciation
            self.data = MediaWikiData(**filtered_data)

            return self.data


class MediaWikiData:
    """
    Custom class handling data formating from a MediaWiki API search
    """

    def __init__(self, title, pageid, url, extract):
        self.title = title
        self.pageid = pageid
        self.url = url
        self.extract = extract

    def __str__(self):
        attributes = {
            "title": self.title,
            "pageid": self.pageid,
            "url": self.url,
            "extract": self.extract
        }

        return str(attributes)
