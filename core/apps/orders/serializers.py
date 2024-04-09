from rest_framework import serializers
from .models import (
    Order,
    OrderStatus,
)
from core.apps.books.serializers import BookSerializer
from core.apps.users.serializers import UserSerializer


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    status = OrderStatusSerializer()
    user = UserSerializer()
    book = BookSerializer()
    class Meta:
        model = Order
        fields = '__all__'