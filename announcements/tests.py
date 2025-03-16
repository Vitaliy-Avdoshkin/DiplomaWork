from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from announcements.models import Announcement, Review
from users.models import User


class AnnouncementTestCase(APITestCase):
    """Тестирование CRUD для объявлений"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.announcements = Announcement.objects.create(
            title="ТЕСТо", price=123, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_announcement_retrieve(self):
        """Тестирование просмотра одного объявления"""
        url = reverse(
            "announcements:announcement-detail", args=(self.announcements.pk,)
        )
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.announcements.title)

    def test_announcement_create(self):
        """Тестирование создания объявления"""
        url = reverse("announcements:announcement-list")
        data = {"title": "ТЕСТо", "description": "атТЕСТат", "price": 100}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get("owner"), self.user.pk)
        self.assertEqual(Announcement.objects.all().count(), 2)

    def test_announcement_update(self):
        """Тестирование обновления объявления"""
        url = reverse(
            "announcements:announcement-detail", args=(self.announcements.pk,)
        )
        data = {"title": "атТЕСТат"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("title"), "атТЕСТат")

    def test_announcement_delete(self):
        """Тестирование удаление объявления"""
        url = reverse(
            "announcements:announcement-detail", args=(self.announcements.pk,)
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Announcement.objects.count(), 0)

    def test_announcement_list(self):
        """Тестирование вывода списка объявлений"""
        url = reverse("announcements:announcement-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.announcements.pk,
                    "title": "ТЕСТо",
                    "price": 123,
                    "description": None,
                    "created_at": "2025-03-16",
                    "owner": 1,
                },
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class ReviewTestCase(APITestCase):
    """Тестирование CRUD для отзывов"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        ad = self.announcements = Announcement.objects.create(
            title="ТЕСТо", price=123, owner=self.user
        )
        self.review = Review.objects.create(
            text="ТЕСТо",
            announcement=ad,
            owner=self.user,
            created_at={
                "2025-03-16T21:44:19.136423+03:00",
            },
        )
        self.client.force_authenticate(user=self.user)

    def test_review_create(self):
        """Тестирование создания отзыва"""
        url = reverse("announcements:review_create")
        data = {"text": "Отлично", "announcement": self.announcements.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get("owner"), self.user.pk)
        self.assertEqual(Announcement.objects.all().count(), 1)

    def test_review_update(self):
        """Тестирование обновления отзыва"""
        url = reverse("announcements:review_update", args=(self.announcements.pk,))
        data = {"text": "Не отлично"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("text"), "Не отлично")

    def test_review_delete(self):
        """Тестирование удаление отзыва"""
        url = reverse("announcements:review_delete", args=(self.announcements.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0)
