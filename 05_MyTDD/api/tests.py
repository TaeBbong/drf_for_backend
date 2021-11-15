from django.test import TestCase
from .models import Book

from rest_framework.test import APIClient
from rest_framework import status


class ModelTest(TestCase):
    def setUp(self):
        self.book_title = "My Book"
        self.book_author = "TaeBbong"
        self.book = Book(title=self.book_title, author=self.book_author)

    def test_model_can_create_a_bucketlist(self):
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {'title': 'My Book 2', 'author': 'TaeBbong'}
        self.response = self.client.post('/api/books/',
                                         self.book_data,
                                         format="json")

    def test_api_can_create_a_book(self):
        print(self.response.content)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)