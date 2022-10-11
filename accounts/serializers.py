from pyexpat import model
from rest_framework import serializers
from .models import User, question_model, answer_model
from django.contrib.auth import get_user_model
User = get_user_model()


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class question_serializer(serializers.ModelSerializer):
    
    questions = user_serializer(many = True, read_only=True)
    
    class Meta:
        model = question_model
        fields = '__all__'


class answer_serializer(serializers.ModelSerializer):
    
    answers = question_serializer(many = True, read_only = True)
    users = user_serializer(many = True, read_only = True)

    class Meta:
        model = answer_model
        fields = '__all__'
