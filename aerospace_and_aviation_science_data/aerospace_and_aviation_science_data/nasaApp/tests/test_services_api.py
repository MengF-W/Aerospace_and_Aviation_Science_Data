import json
from unittest.mock import patch
from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import os


# Create your tests here.

class ApodServicesApiTest(APITestCase):
    def setUp(self):

        self.client = Client()

        with open(os.path.join(os.path.dirname(__file__),'templates', 'example_data.json'), "r") as file:

            self.mock_response_data = json.load(file)

    @patch('nasaApp.services.ApodServices.get_apod_basic')
    def test_get_apod_api(self,mock_get_apod_basic):
        mock_get_apod_basic.return_value = self.mock_response_data
        response = self.client.get(reverse('apod_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(json.loads(response.content.decode('utf-8'))['result_list'])