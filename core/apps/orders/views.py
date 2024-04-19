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
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from core.apps.users.models import User
from core.apps.books.models import Book


class OrderAPIView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request):
        access_token = request.headers.get('Authorization').split(' ')[1] 
        print('MyAccess Token:', access_token) 

        try:
            token = AccessToken(access_token)
            user_id = token.payload['user_id']
            user = User.objects.get(pk=user_id)
            orders = Order.objects.filter(user=user)
            serializer = self.serializer_class(orders, many=True)
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():  
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class OrderStatusListAPIView(ListAPIView):
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()


    