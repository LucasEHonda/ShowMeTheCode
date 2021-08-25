import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class TestCall(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "candidato@vizir.com", "admin12345"
        )
        self.client = APIClient()

    def test_should_return_unauthorized(self):
        """Test that login is required for retrieving calls"""
        response = self.client.get(reverse("calls-list"))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_return_authorized(self):

        self.client.force_authenticate(self.user)

        response = self.client.get(reverse("calls-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, [])

    def test_create_call(self):
        self.client.force_authenticate(self.user)

        data = {
            "origin": "011",
            "destiny": "016",
            "talk_more_tariff": 0,
            "default_tariff": 0,
            "plan": "",
            "minutes": 1,
        }

        response = self.client.post("/calls/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content.decode()),
            {
                "origin": "011",
                "destiny": "016",
                "talk_more_tariff": 0.0,
                "default_tariff": 1.9,
                "minutes": 1,
            },
        )
