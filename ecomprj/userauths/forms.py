from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths import models

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = models.User
        fields = ['username', 'email'] 
