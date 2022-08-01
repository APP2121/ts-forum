from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserModel
from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import FileInput


class UserModelForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['full_name', 'date_of_birth', 'contact_number', 'about', 'company_name', 'designation']
        exclude = ['user']
        widgets = {
         'profile_img': FileInput(),
         }

class ProfileUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = '__all__'
