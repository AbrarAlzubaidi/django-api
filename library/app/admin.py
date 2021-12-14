from django.contrib import admin
from .models import Book


@admin.register(Book)
class PostBook(admin.ModelAdmin):
    list_display = ['title', 'auther', 'rate','created_day','updated']