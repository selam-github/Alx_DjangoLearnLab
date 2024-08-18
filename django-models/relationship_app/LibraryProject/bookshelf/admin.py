from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication year in the list view
    list_display = ('title', 'author', 'publication_year')
    # Add filters for publication year and author
    list_filter = ('publication_year', 'author')
    
    # Enable search functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin configuration
admin.site.register(Book, BookAdmin)