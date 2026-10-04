import json
from unittest.mock import patch, MagicMock
from django.test import TestCase
from nasaApp import services
import os


# Create your tests here.

class ApodServicesTest(TestCase):
    def setUp(self):

        with open(os.path.join(os.path.dirname(__file__),'templates', 'example_data.json'), "r") as file:

            self.mock_response_data = json.load(file)

    def test_get_apod_basic(self):
        mock_api_client = MagicMock()
        mock_api_client.get.return_value.json.return_value = self.mock_response_data
        result_item_list = services.ApodServices.get_apod_basic(mock_api_client)

        mock_api_client.get.assert_called_once_with('https://science.nasa.gov/wp-json/wp/v2/apod-basic')
        self.assertGreater(len(result_item_list), 0)

        for result in result_item_list:
            match result["media_type"]:
                case "image":
                    self.assertEqual(result['media_location'], '<IMG SRC="exampleContentUrl"alt=exampleAlt width="200" height="300">')
                case "video":
                    self.assertEqual(result['media_location'], '<source src="exampleVideoUrl" type="video/mp4">')
