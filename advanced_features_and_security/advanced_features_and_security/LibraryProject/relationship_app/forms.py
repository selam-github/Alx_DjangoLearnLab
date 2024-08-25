from django import forms
from .models import Book  # Import your Book model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', ]