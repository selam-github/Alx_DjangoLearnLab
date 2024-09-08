# BookListView: Retrieves a list of all books from the database. Read-only access is allowed for unauthenticated users.
# BookDetailView: Retrieves the details of a specific book by its primary key (ID).
# BookCreateView: Allows authenticated users to create new books. Ensures that the publication year is not in the future.
# BookUpdateView: Allows authenticated users to update the details of an existing book.
# BookDeleteView: Allows authenticated users to delete a book from the database.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.exceptions import ValidationError
from datetime import date
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters

# ListView: Retrieve all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filter by title, author, and publication year
    search_fields = ['title', 'author__name']  # Search in title and author's name
    ordering_fields = ['title', 'publication_year']  # Order by title and publication year

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create
    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update
    

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete
