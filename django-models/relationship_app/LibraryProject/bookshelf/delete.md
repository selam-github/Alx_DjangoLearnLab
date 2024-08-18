from bookshelf.models import Book
# Deleting the book instance
book.delete()

# Verifying the deletion by trying to retrieve all books
books = Book.objects.all()


## Expected Output
>>> books
<QuerySet []>