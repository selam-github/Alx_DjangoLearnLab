
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):###BookViewSet for hanadiling CRUD opeation 
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

