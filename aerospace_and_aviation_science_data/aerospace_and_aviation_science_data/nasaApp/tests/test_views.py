import os

from django.test import TestCase, RequestFactory
import json
from nasaApp import views
from unittest.mock import patch


class ApodViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        with open(os.path.join(os.path.dirname(__file__),'templates', 'example_data.json'), "r") as file:

            self.mock_response_data = json.load(file)

    @patch('nasaApp.services.ApodServices.get_apod_basic')
    def test_get_apod_view(self,mock_get_apod_basic):
        mock_get_apod_basic.return_value = self.mock_response_data
        request = self.factory.get('')
        response = views.apod(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("The NASA Astronomy Picture of the Day List" in response.content.decode("utf-8"))

