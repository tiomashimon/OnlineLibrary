from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    # CreateAPIView,
    # UpdateAPIView,
    # RetrieveAPIView,
    # DestroyAPIView,
    ListAPIView
)
from .models import (
    Book,
    BookGenre,
    BookStatus,
    BookType,
    Fine
)
from .serializers import (
    BookSerializer,
    BookGenreSerializer,
    BookStatusSerializer,
    BookTypeSerializer,
    FineSerializer,
)


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookStatusListAPIView(ListAPIView):
    serializer_class = BookStatusSerializer
    queryset = BookStatus.objects.all()


class BookTypeListAPIView(ListAPIView):
    serializer_class = BookTypeSerializer
    queryset = BookType.objects.all()


class BookGenreListAPIView(ListAPIView):
    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()


class   FineListAPIView(ListAPIView):
    serializer_class = FineSerializer
    queryset = Fine.objects.all()



