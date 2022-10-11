from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from django import forms
from accounts.models import question_model, answer_model, User
from django.contrib.auth import get_user_model
User = get_user_model()


class user_model_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'nick_name', 'contact_number', 'about', 'date_of_birth', 'company_name', 'designation' ]

class userProfile_form(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class question_form(forms.ModelForm):
    status_option = [('active', 'Active'), ('inactive', 'Inactive')]
    status_name = forms.CharField(widget=forms.Select(choices = status_option))
    class Meta:
        model = question_model
        fields = ['question_title', 'question_description', 'technology_name',]

class answer_form(forms.ModelForm):
    
    class Meta:
        model = answer_model
        fields = ('answer',)

        widgets = {
            'answer': forms.Textarea(attrs={'class':'input','style':'width:800px; height:100px; border-radius:5px; padding-top:10px; ',  'placeholder':'Provide Your Answer'})
        }

