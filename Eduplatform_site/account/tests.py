from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

USER_DATA = {"email": "test_user@test.ru", "password": "123456", "first_name": "Test", "last_name": "Test"}


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse("create_user")
        response = self.client.post(url, data=USER_DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
