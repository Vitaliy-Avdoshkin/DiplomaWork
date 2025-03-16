from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тестирование CRUD для пользователей"""

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com", first_name="TEST", last_name="TSET"
        )
        self.client.force_authenticate(user=self.user)

    def test_user_retrieve(self):
        """Тестирование просмотра информации об одном пользователе"""
        url = reverse("users:user-profile-detail", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("first_name"), self.user.first_name)

    def test_user_create(self):
        """Тестирование создания пользователя"""
        url = reverse("users:register")
        data = {
            "email": "testnew@test.ru",
            "password": "Qwerty123",
            "first_name": "Test",
            "last_name": "Test",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get("first_name"), "Test")
        self.assertEqual(User.objects.all().count(), 2)

    def test_user_update(self):
        """Тестирование обновления пользователя"""
        url = reverse("users:user-profile-detail", args=(self.user.pk,))
        data = {"first_name": "TestY"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("first_name"), "TestY")

    def test_user_delete(self):
        """Тестирование удаление пользователя"""
        url = reverse("users:user-profile-detail", args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
