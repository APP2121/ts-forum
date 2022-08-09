from pyexpat import model

from django import forms
from QA_App.models import question_model, answer_model, user_model

class user_model_form(forms.ModelForm):
    class Meta:
        model = user_model
        fields = '__all__'

class question_form(forms.ModelForm):
    class Meta:
        model = question_model
        fields = '__all__'


class answer_form(forms.ModelForm):
    class Meta:
        model = answer_model
        fields = "__all__"