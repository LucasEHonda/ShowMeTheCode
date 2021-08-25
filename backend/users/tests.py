import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class TestUser(TestCase):
    def setUp(self) -> None:
        self.data = {
            "username": "candidato@vizir.com",
            "email": "candidato@vizir.com",
            "password": "vizir12345",
        }
        return super().setUp()

    def test_create_user(self):
        """Test should create user"""
        response = self.client.post("/create/", self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user_token(self):
        """Test should create user and get her token"""
        response = self.client.post("/create/", self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post("/token/", self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_return_unauthorized(self):
        """Test that login is required for retrieving user"""
        response = self.client.get(reverse("me"))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
