import pytest
import json
from io import BytesIO

import urllib.request

from gpb_app.utils import utils


class TestGMapsRequest:
    def setup_method(self):
        self.address = "7 cité Paradis, Paris"
        self.address_query = self.address.lower().split()
        self.address_query = "+".join(self.address_query)

        self.address_lat = 48.8747265
        self.address_lng = 2.3505517
        self.gmapsrequest = utils.GMapsRequest(self.address)
        self.gmaps_filtered_data = {
            'address': '7 Cité Paradis, 75010 Paris, France',
            'lat': 48.8747265,
            'lng': 2.3505517,
            'place_id': 'ChIJxfB-lhRu5kcRfK7MP5oTfH8',
        }

        with open(
            "gpb_app/data/gmaps_mock.json", "r", encoding="utf8"
        ) as mockfile:
            self.gmaps_mock_data = json.load(mockfile)

    def test_instance(self):
        """
        :Test success conditions:
        The data returned is a valid GMapsRequest object
        """
        assert(isinstance(self.gmapsrequest, utils.GMapsRequest))

    def test_search(self, monkeypatch):
        """
        :Test success conditions:
        The Google Maps API returns a JSON result fitting expectations.
        Mocks http request via urllib.request module
        """

        # Replace requests return by a json mock stored locally
        def mockreturn(url):
            return BytesIO(json.dumps(self.gmaps_mock_data).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert self.gmaps_mock_data == self.gmapsrequest.search()

    def test_lat_lng_values(self):
        """
        :Test success conditions:
        The latitude and longitude are the same as in the mock data file
        The type of the latitude and longitude attrs is float
        """

        # Test latitude and longitude values
        assert(type(self.address_lat) is float)
        assert(type(self.address_lng) is float)
        assert(self.address_lat == self.gmaps_mock_data["results"][0][
            "geometry"]["location"]["lat"])

        assert(self.address_lng == self.gmaps_mock_data["results"][0][
            "geometry"]["location"]["lng"])

    def test_filter_data_from_gmaps(self):
        self.gmapsrequest.search()
        assert(str(self.gmaps_filtered_data) == str(
            self.gmapsrequest.filter_data())
        )


if __name__ == "__main__":
    pytest.main()
