
from bookshelf.models import Book

# Creating a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
## Expected Output
>>> book
<Book: 1984>