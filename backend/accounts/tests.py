from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


User = get_user_model()


class AuthenticationApiTests(APITestCase):
    def test_register_returns_tokens(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "student1",
                "email": "student1@example.com",
                "password": "ComplexPass123",
                "role": "student",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertTrue(User.objects.filter(username="student1").exists())
