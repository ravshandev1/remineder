from rest_framework import serializers, exceptions
from .models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'image', 'password', 'password2']

    password2 = serializers.CharField()

    def validate(self, attrs):
        pas1 = attrs['password']
        pas2 = attrs['password2']
        if pas1 != pas2:
            raise exceptions.ValidationError({
                'message': "Passwords did not match"
            })
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'image']
