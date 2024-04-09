from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import (
    UserSerializer, 
    UserCharacteristicsSerializer,
)
from .models import (
    User,
    UserCharacteristics,
)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()



class UserCharacteristicsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserCharacteristicsSerializer
    queryset = UserCharacteristics.objects.all()



