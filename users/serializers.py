from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        read_only_fields = []
        fields = [
            "email",
            "password",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}


    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        if not password:
            raise serializers.ValidationError({"password": "Введите пароль"})
        user = User(email=email)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', ]

