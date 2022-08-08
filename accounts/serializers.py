from rest_framework import serializers
from . models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'full_name', 'contact_number','about',
        'date_of_birth','company_name','designation']
        read_only_fields = ('pk', 'username', 'email',)
