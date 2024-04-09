from django.urls import path
from .views import (
    OrderAPIView,
    OrderStatusListAPIView,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', OrderAPIView, basename='order')


urlpatterns = [
    path('list/', OrderStatusListAPIView.as_view(), name='status-list'),

]

urlpatterns += router.urls