from .models import Book
from rest_framework import generics
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset  = Book.objects.all()
    # to filter data by title
    # queryset  = Book.objects.filter(title= 'something')
    serializer_class  = BookSerializer

# RetrieveUpdateView --> for just update requset
# RetrieveUpdateDestroyAPIView---> for RUD: retrive, update, delete
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Book.objects.all()
    serializer_class  = BookSerializer