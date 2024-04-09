from rest_framework import serializers
from .models import (
    Book,
    BookGenre,
    BookStatus,
    BookType,
    Fine
)
from core.apps.users.serializers import UserSerializer



class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = '__all__'

class BookStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStatus
        fields = '__all__'

class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = '__all__'

class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    genre = BookGenreSerializer()
    status = BookStatusSerializer()
    type = BookTypeSerializer()
    
    class Meta:
        model = Book
        fields = '__all__'