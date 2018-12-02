from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.utils import json

from ..models import User
from ..serializers import UserSerializer


class GetUserDetailTest(APITestCase):
    """Test module for GET user detail API.
    """
    client = APIClient()
    path = '/users/{id}'

    def setUp(self):
        self.user = User.objects.create(
            email='user@mail.com',
            first_name='Иван',
            last_name='Иванов',
            gender='m',
            birth_date=-852940800)

    def test_get_valid_user(self):
        response = self.client.get(self.path.format(id=self.user.id))
        user = User.objects.get(id=self.user.id)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_user(self):
        pk = 30
        response = self.client.get(self.path.format(id=pk))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewUserTest(APITestCase):
    """Test module for inserting a new user.
    """
    client = APIClient()
    path = '/users/new'
    content_type = 'application/json'

    def setUp(self):
        self.valid_payload = {
            'id': 125,
            'email': 'foobar@mail.ru',
            'first_name': 'Маша',
            'last_name': 'Пушкина',
            'gender': 'f',
            'birth_date': 365299200,
        }
        self.invalid_payload = {
            'id': 140,
            'email': '',
            'first_name': '',
            'last_name': 'Иванов',
            'gender': 'm',
        }

    def test_create_user(self):
        response = self.client.post(
            path=self.path,
            data=json.dumps(self.valid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Повторное создание пользователя с существующим id в БД.
        response = self.client.post(
            path=self.path,
            data=json.dumps(self.valid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_user(self):
        response = self.client.post(
            path=self.path,
            data=json.dumps(self.invalid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleUserTest(APITestCase):
    """Test module for updating an existing user record.
    """
    client = APIClient()
    path = '/users/{id}'
    content_type = 'application/json'

    def setUp(self):
        params = {
            'email': 'foobar@mail.ru',
            'first_name': 'Маша',
            'last_name': 'Пушкина',
            'gender': 'f',
            'birth_date': 365299200,
        }
        self.valid_payload = {
            'email': 'new@mail.ru',
            'first_name': 'Маша',
            'last_name': 'Кукушкина',
            'gender': 'f',
            'birth_date': 365299200,
        }
        self.invalid_payload = {
            'email': '',
            'first_name': '',
            'last_name': 'Иванов',
            'gender': 'm',
        }
        self.user = User.objects.create(**params)

    def test_valid_update_user(self):
        response = self.client.put(
            path=self.path.format(id=self.user.id),
            data=json.dumps(self.valid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_user(self):
        response = self.client.put(
            path=self.path.format(id=self.user.id),
            data=json.dumps(self.invalid_payload),
            content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
