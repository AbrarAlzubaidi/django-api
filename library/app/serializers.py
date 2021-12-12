from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title','description','auther','rate','created_day','updated']
        model = Book