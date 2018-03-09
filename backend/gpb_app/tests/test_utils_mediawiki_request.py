import pytest
import json
from io import BytesIO

import urllib.request

from gpb_app.utils import utils


class TestMediawikiRequest:
    def setup_method(self):
        """
        Set some needed fixed data for the tests.
        """
        self.address_lat = 48.8747265
        self.address_lng = 2.3505517
        self.random_place = 0
        self.mediawikirequest = utils.MediaWikiRequest(self.address_lat, self.address_lng, random_place=self.random_place)

        with open("gpb_app/data/mediawiki_geosearch_mock.json", "r", encoding="utf8") as mockfile:
            self.mediawiki_geosearch_mock_data = json.load(mockfile)

        with open("gpb_app/data/mediawiki_extracts_mock.json", "r", encoding="utf8") as mockfile:
            self.mediawiki_extracts_mock_data = json.load(mockfile)

    def test_instance(self):
        """
        :Test success conditions:
        The data returned is a valid MediaWikiRequest object
        """
        assert(isinstance(self.mediawikirequest, utils.MediaWikiRequest))

    def test_geo_search(self, monkeypatch):
        """
        :Test success conditions:
        The MediaWiki API returns a JSON result fitting expectations.
        Mocks http request via urllib.request module
        """
        def mockreturn(url):
            return BytesIO(json.dumps(self.mediawiki_geosearch_mock_data).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert self.mediawiki_geosearch_mock_data == self.mediawikirequest.geo_search()

    def test_get_extracts(self, monkeypatch):
        """
        :Test success conditions:
        The Extracts API returns a JSON result fitting expectations.
        Mocks http request via urllib.request module
        IMPORTANT : random_place must be set to 0 in the instanciation ↑
        """
        def mockreturn(url):
            return BytesIO(json.dumps(self.mediawiki_geosearch_mock_data).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        self.mediawikirequest.geo_search()
        self.mediawikirequest.get_extracts()

        assert self.mediawiki_extracts_mock_data == self.mediawikirequest.get_extracts()

    def test_get_data(self, monkeypatch):
        """
        :Test success conditions:
        The data returned is a valid WikiMediaData object
        """
        assert isinstance(self.mediawikirequest.get_data(), utils.MediaWikiData)


if __name__ == "__main__":
    pytest.main()
