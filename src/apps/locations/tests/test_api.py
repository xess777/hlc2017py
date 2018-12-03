from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.utils import json

from ..models import Location
from ..serializers import LocationSerializer


class GetLocationDetailTest(APITestCase):
    """Test module for GET location detail API.
    """
    client = APIClient()
    path = '/locations/{id}'

    def setUp(self):
        self.location = Location.objects.create(
            place='Ручей',
            country='Италия',
            city='Ньюлёв',
            distance=15)

    def test_get_valid_location(self):
        response = self.client.get(self.path.format(id=self.location.id))
        location = Location.objects.get(id=self.location.id)
        serializer = LocationSerializer(location)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_location(self):
        pk = 30
        response = self.client.get(self.path.format(id=pk))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewLocationTest(APITestCase):
    """Test module for inserting a new location.
    """
    client = APIClient()
    path = '/locations/new'
    content_type = 'application/json'

    def setUp(self):
        self.valid_payload = {
            'distance': 15,
            'city': 'Ньюлёв',
            'place': 'Ручей',
            'id': 1,
            'country': 'Италия',
        }
        self.invalid_payload = {
            'city': '',
            'place': '',
            'id': 2,
            'country': '',
        }

    def test_create_location(self):
        response = self.client.post(
            path=self.path,
            data=json.dumps(self.valid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Повторное создание записи с существующим id в БД.
        response = self.client.post(
            path=self.path,
            data=json.dumps(self.valid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_location(self):
        response = self.client.post(
            path=self.path,
            data=json.dumps(self.invalid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleLocationTest(APITestCase):
    """Test module for updating an existing location record.
    """
    client = APIClient()
    path = '/locations/{id}'
    content_type = 'application/json'

    def setUp(self):
        params = {
            'distance': 15,
            'city': 'Ньюлёв',
            'place': 'Ручей',
            'id': 1,
            'country': 'Италия',
        }
        self.valid_payload = {
            'distance': 10,
            'city': 'Ньюлёв',
            'place': 'Ручей',
            'country': 'Италия',
        }
        self.invalid_payload = {
            'distance': 20,
            'city': '',
            'place': '',
            'country': '',
        }
        self.location = Location.objects.create(**params)

    def test_valid_update_location(self):
        response = self.client.put(
            path=self.path.format(id=self.location.id),
            data=json.dumps(self.valid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_location(self):
        response = self.client.put(
            path=self.path.format(id=self.location.id),
            data=json.dumps(self.invalid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
