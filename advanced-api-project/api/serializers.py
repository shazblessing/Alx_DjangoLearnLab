from .models import Book, Author
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields= '__all__'

    def validate_publication_year(self, value):  # Custom validation to ensure publication year is not in the future
        if value > 2024:
            raise serializers.ValidationError('publication can not be in the future')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books= BookSerializer(many=True, read_only=True) # NESTED SERIALIZER TO SHOW RELATED BOOKS
    class Meta: 
        model = Book
        fields= 'name'        

