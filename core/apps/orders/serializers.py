from rest_framework import serializers
from .models import (
    Order,
    OrderStatus,
)
from core.apps.books.models import Book
from core.apps.users.models import User


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    status = OrderStatusSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())


    class Meta:
        model = Order
        fields = '__all__'


