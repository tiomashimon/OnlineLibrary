from django.urls import path
from .views import (
    UserCharacteristicsRetrieveUpdateAPIView,
    UserRetrieveUpdateAPIView,
)


urlpatterns = [
    path('<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('stats/<int:pk>/', UserCharacteristicsRetrieveUpdateAPIView.as_view(), name='user-characteristics'),

]
