from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Book(models.Model):
    title=models.CharField(max_length=200)
    publication_year= models.IntegerField(max_length=100)
    author=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    