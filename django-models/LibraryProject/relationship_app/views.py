from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library



#Implement Function-based View:
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", "Book.objects.all()")

# Implementing the Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html' # Optional: Define a template for HTML rendering
    context_object_name = 'library'
