# The BookSerializer handles serialization of the Book model, including custom validation to
# ensure that the publication year is not in the future.
# The AuthorSerializer includes a nested BookSerializer to serialize related books.

from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        from datetime import date
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']