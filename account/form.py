from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreateFM(UserCreationForm):
    username = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
        required = ('first_name',)