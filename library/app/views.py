from .models import Book
from rest_framework import generics
from .serializers import BookSerializer
from .permisiions import  ReadOnly,IsAuthenticated
# from rest_framework.permissions import IsAuthenticated


class BookCreateView(generics.CreateAPIView):
    queryset  = Book.objects.all()
    permission_classes = [IsAuthenticated]
    # to filter data by title
    # queryset  = Book.objects.filter(title= 'something')
    serializer_class  = BookSerializer

class BookListView(generics.ListAPIView):
    queryset  = Book.objects.all()
    permission_classes = (ReadOnly,)
    # to filter data by title
    # queryset  = Book.objects.filter(title= 'something')
    serializer_class  = BookSerializer

# RetrieveUpdateView --> for just update requset
# RetrieveUpdateDestroyAPIView---> for RUD: retrive, update, delete
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Book.objects.all()
    permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class  = BookSerializer
