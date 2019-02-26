from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username','phone','full_name')

class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id,''full_name','username','phone','email','is_active')

class UserNameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    
    def validate(self,attrs):
        if not User.objects.filter(username=attrs['username']).exists():
            raise CommonException(detail=USER_DOES_NOT_EXISTS)
        if not User.objects.filter(username=attrs['username']).first().is_active:
            raise CommonException(detail=USER_NOT_ACTIVE)
        return attrs