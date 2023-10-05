from django import forms as f
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = f.CharField(max_length=100, required=True, widget=f.TextInput())
    email = f.CharField(max_length=100, required=True, widget=f.TextInput())
    password1 = f.CharField(max_length=50, required=True, widget=f.PasswordInput())
    password2 = f.CharField(max_length=50, required=True, widget=f.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]
