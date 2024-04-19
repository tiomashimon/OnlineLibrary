from .models import (
    User,
    UserCharacteristics,
    Notification,
    NotificationType,
)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', ]
        


class UserCharacteristicsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = '__all__'
        model = UserCharacteristics


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = NotificationType
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    type = NotificationTypeSerializer()
    class Meta: 
        model = Notification
        fields = '__all__'