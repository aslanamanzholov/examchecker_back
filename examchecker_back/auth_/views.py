from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (UserSerializer, UserNameSerializer)
from .token import get_token
from .models import (MainUserManager, MainUser)

User = get_user_model

class AuthViewSet(viewsets.GenericViewSet):
    queryset = MainUserManager.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['get','post']

    def get_serializer_class(self):
        if self.action == 'login':
            return UserNameSerializer
        return MainUserManager

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = UserNameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.validated_data['username'])
        return Response({})

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', ]
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False)
    def get(self, request):
        return Response({'user': UserSerializer(request.user).data})

    @action(methods=['get'], detail=False)
    def logout(self, request):
        return Response({})   