from django.db import models
from django.contrib.auth import get_user_model

class Auther(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    location = models.TextField()
    created_day = models.DateTimeField(auto_now = True, auto_now_add=False)
    updated = models.DateTimeField(auto_now = False, auto_now_add=True)

    def __str__(self):
         return self.name

         
class Book(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField()
    auther = models.ForeignKey(get_user_model(), on_delete= models.CASCADE) 
    rate = models.FloatField()
    created_day = models.DateTimeField(auto_now = True, auto_now_add=False)
    updated = models.DateTimeField(auto_now = False, auto_now_add=True)

    def __str__(self):
         return self.title
