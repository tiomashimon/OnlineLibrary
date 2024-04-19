from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    # CreateAPIView,
    # UpdateAPIView,
    # RetrieveAPIView,
    # DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
)
from .models import (
    Book,
    BookGenre,
    BookStatus,
    BookType,
    Fine,
    Like,
)
from .serializers import (
    BookSerializer,
    BookGenreSerializer,
    BookStatusSerializer,
    BookTypeSerializer,
    FineSerializer,
    LikeSerializer,
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from core.apps.users.models import User

from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django.db.models import F


class BookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(available_copies__gte=1).order_by('title')

    pagination_class = BookPagination
    search_fields = ['title',]
    filter_backends = (filters.SearchFilter,)


class BookStatusListAPIView(ListAPIView):
    serializer_class = BookStatusSerializer
    queryset = BookStatus.objects.all()


class BookTypeListAPIView(ListAPIView):
    serializer_class = BookTypeSerializer
    queryset = BookType.objects.all()


class BookGenreListAPIView(ListAPIView):
    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()


class  FineListAPIView(ListAPIView):
    serializer_class = FineSerializer

    def get(self, request):
        access_token = request.headers.get('Authorization').split(' ')[1] 
        print('LikeAccess Token:', access_token) 

        try:
            token = AccessToken(access_token)
            user_id = token.payload['user_id']
            user = User.objects.get(pk=user_id)
            fines = Fine.objects.filter(user=user)
            serializer = self.serializer_class(fines, many=True)
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        

class LikeListCreateAPIView(ListCreateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def get(self, request):
        access_token = request.headers.get('Authorization').split(' ')[1] 
        print('LikeAccess Token:', access_token) 

        try:
            token = AccessToken(access_token)
            user_id = token.payload['user_id']
            user = User.objects.get(pk=user_id)
            likes = Like.objects.filter(user=user)
            serializer = self.serializer_class(likes, many=True)
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
    
    def post(self, request):
        book_id = request.data.get('book')
        user_id = request.data.get('user')

        existing_like = Like.objects.filter(user_id=user_id, book_id=book_id).first()
        if existing_like:
            existing_like.delete()
            return Response({'message': 'Like deleted successfully'}, status=200)
        else:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)





