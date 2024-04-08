from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path
from .views import (
    BookGenreListAPIView,
    BookStatusListAPIView,
    BookTypeListAPIView,
    FineListAPIView,
)


router = DefaultRouter()

router.register('', BookViewSet, basename='book')

urlpatterns = [
    path('genres/', BookGenreListAPIView.as_view(), name='genre-list'),
    path('statuses/', BookStatusListAPIView.as_view(), name='status-list'),
    path('types/', BookTypeListAPIView.as_view(), name='type-list'),
    path('fines/', FineListAPIView.as_view(), name='fine-list'),
]

urlpatterns += router.urls