from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import CustomUser
from .models import Book
from .forms import ExampleForm
from .forms import BookSearchForm


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
def search_books(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data.get('query')
        books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})


def your_view(request):
    form = ExampleForm()
    # Your view logic here
    return render(request, 'your_template.html', {'form': form})

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data, e.g., create or update a model instance
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            publication_year = form.cleaned_data['publication_year']
            # Example: Create a new Book instance (if applicable)
            # Book.objects.create(title=title, author=author, publication_year=publication_year)
            # Redirect or render a success page
            return redirect('success_url')  # Update with your success URL
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})


