from django import forms
from django.contrib.auth.forms import UserCreationForm
from grade_app.models import User_model

class User_register_form(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput) 
    class Meta:
        model = User_model
        fields = ('username','password1','password2')






