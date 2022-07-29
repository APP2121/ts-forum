from rest_framework import serializers
from . models import UserModel
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        #fields = ['username', 'email', 'password1', 'password2']
        fields='__all__'
