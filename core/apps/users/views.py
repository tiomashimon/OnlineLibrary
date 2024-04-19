from rest_framework.generics import (
    RetrieveUpdateAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from .serializers import (
    UserSerializer, 
    UserCharacteristicsSerializer,
    NotificationSerializer,
)
from .models import (
    User,
    UserCharacteristics,
    Notification,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        access_token = request.headers.get('Authorization').split(' ')[1] 
        print('Access Token:', access_token) 

        try:
            token = AccessToken(access_token)
            user_id = token.payload['user_id']
            user = User.objects.get(pk=user_id)
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class UserCharacteristicsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserCharacteristicsSerializer
    queryset = UserCharacteristics.objects.all()

    
class NotificationsListAPIVIew(ListAPIView):
    serializer_class = NotificationSerializer
    
    def get(self, request):
        access_token = request.headers.get('Authorization').split(' ')[1] 
        print('NotAccess Token:', access_token) 

        try:
            token = AccessToken(access_token)
            user_id = token.payload['user_id']
            user = User.objects.get(pk=user_id)
            likes = Notification.objects.filter(user=user).order_by('-created_at')
            serializer = self.serializer_class(likes, many=True)
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)