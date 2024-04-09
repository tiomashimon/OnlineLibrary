from .models import (
    User,
    UserCharacteristics,
)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class UserCharacteristicsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = '__all__'
        model = UserCharacteristics