from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .consts import USER_DATA


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse("user-list")
        response = self.client.post(url, data=USER_DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
