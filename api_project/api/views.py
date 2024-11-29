from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from serializers import Bookserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer