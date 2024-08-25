from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import CustomUser
from .models import Book
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def view_item(request):
    # Your view logic for viewing items
    return render(request, 'bookshelf/view_item.html')

@permission_required('bookshelf.can_create', raise_exception=True)
def create_item(request):
    # Your view logic for creating items
    return render(request, 'bookshelf/create_item.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_item(request, item_id):
    # Your view logic for editing items
    return render(request, 'bookshelf/edit_item.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_item(request, item_id):
    # Your view logic for deleting items
    return redirect('bookshelf:view_item')

def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})

def your_view(request):
    form = ExampleForm()

    return render(request, 'your_template.html', {'form': form})


