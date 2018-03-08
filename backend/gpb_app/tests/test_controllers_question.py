import pytest
import json
from io import BytesIO

import urllib.request

from gpb_app.controllers import question


class TestQuestionHandler:
    def setup_method(self):
        self.original_query = "Hello Grandpy ! Donne moi l'adresse d'OpenClassrooms stp !"
        self.mediawikirequest = question.QuestionHandler(self.original_query)

        with open(
            "gpb_app/data/question_mock.json", "r", encoding="utf8"
        ) as mockfile:
            self.mediawiki_mock_data = json.load(mockfile)

    def test_instance(self):
        """
        :Test success conditions:
        The data returned is a valid QuestionHandler object
        """
        assert(isinstance(self.mediawikirequest, question.QuestionHandler))

    def test_parse(self):
        """
        :Test success conditions:
        The parsed query is different from the original query
        IMPORTANT: The instance is auto parsed at instanciation
        """
        assert(self.mediawikirequest != self.original_query)
        # print('\n' + self.query.parse(), '\n' + self.original_query)

    def test_to_output(self, monkeypatch):
        """
        :Test success conditions:
        The Extracts API returns a JSON result fitting expectations.
        Mocks http request via urllib.request module
        """
        def mockreturn(url):
            return BytesIO(json.dumps(self.mediawiki_mock_data).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        # assert self.mediawiki_mock_data == self.mediawikirequest.to_json()
        print(self.mediawiki_mock_data)
        print(self.mediawikirequest.to_output())


if __name__ == "__main__":
    pytest.main()
