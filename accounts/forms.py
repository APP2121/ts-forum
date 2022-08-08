from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm,UserModel
from .models import User
from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import FileInput

from django import forms

class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'date_of_birth', 'contact_number', 'about', 'company_name', 'designation']
            

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'date_of_birth', 'contact_number', 'about', 'company_name', 'designation']
        exclude = ['user']
        widgets = {
         'profile_img': FileInput(),
         }

class ProfileUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'




