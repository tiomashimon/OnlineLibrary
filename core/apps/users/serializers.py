from .models import (
    User,
    UserCharacteristics,
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