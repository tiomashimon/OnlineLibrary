from django.shortcuts import render
from .serializers import (
    OrderStatusSerializer,
    OrderSerializer,
)
from .models import (
    Order,
    OrderStatus,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView


class OrderAPIView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderStatusListAPIView(ListAPIView):
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()