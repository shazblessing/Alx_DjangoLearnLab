from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        
        # Log in the user
        self.client.login(username="testuser", password="password123")

        # Set up test data
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )
        self.book_url = reverse('book-list')  # Replace 'book-list' with the actual name of your endpoint
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.id})
    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_update_book(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.book_url}?author__name={self.author.name}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_search_books(self):
        response = self.client.get(f"{self.book_url}?search=Potter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")
    def test_order_books_by_publication_year(self):
        Book.objects.create(
            title="Older Book",
            publication_year=1990,
            author=self.author
        )
        response = self.client.get(f"{self.book_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1990)

    def test_create_book_requires_authentication(self):
        self.client.logout()  # Ensure no user is logged in
        data = {"title": "Unauthorized Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)