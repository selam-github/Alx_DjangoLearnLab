from django.db import models

# Create your models here.
# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)
# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE , related_name='Book')
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book,related_name='Libraryclear')

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  # Add this method