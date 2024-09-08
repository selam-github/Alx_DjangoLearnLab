from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Set up user and initial book data
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.login(username='testuser', password='password')  # Log in the user
        self.book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2022)
    
    def test_book_creation(self):
        # Test the creation of a new book
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2021
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Check if the book is added
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_book_retrieve(self):
        # Test retrieval of a single book
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_book_update(self):
        # Test updating a book's details
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'Updated Book'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_book_delete(self):
        # Test book deletion
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        # Test filtering by title
        url = reverse('book-list') + '?title=Test Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return 1 book

    def test_search_books(self):
        # Test searching for books by author
        url = reverse('book-list') + '?search=Test Author'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_ordering_books(self):
        # Test ordering books by publication year
        Book.objects.create(title='Old Book', author='Old Author', publication_year=2000)
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Old Book')  # The oldest book should come first

    def test_permissions(self):
        # Test permissions: ensure only authenticated users can create, update, and delete
        self.client.logout()  # Log out the user
        create_url = reverse('book-create')
        update_url = reverse('book-update', args=[self.book.id])
        delete_url = reverse('book-delete', args=[self.book.id])

        # Create (POST) without authentication
        response = self.client.post(create_url, {'title': 'Unauthorized Book'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Update (PATCH) without authentication
        response = self.client.patch(update_url, {'title': 'Unauthorized Update'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Delete (DELETE) without authentication
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
