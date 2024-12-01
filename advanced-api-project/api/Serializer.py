from .models import Book, Author
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields= '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books= BookSerializer(many=True, read_only=True) # NESTED SERIALIZER TO SHOW RELATED BOOKS
    class Meta: 
        model = Book
        fields= 'name'        

