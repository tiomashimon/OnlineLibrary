from django.urls import path
from .views import (
    UserCharacteristicsRetrieveUpdateAPIView,
    UserCreateAPIView,
    UserRetrieveAPIView,
    NotificationsListAPIVIew,
    UserListAPIView,
)


urlpatterns = [
    
    path('stats/<int:pk>/', UserCharacteristicsRetrieveUpdateAPIView.as_view(), name='user-characteristics'),
    path('create/', UserCreateAPIView.as_view(), name='create-user'),
    path('notifications/', NotificationsListAPIVIew.as_view(), name='list-notifications'),
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('', UserRetrieveAPIView.as_view(), name='user-retrueve',),
    
]
