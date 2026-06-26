from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PasswordEntry

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PasswordEntryForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    class Meta:
        model = PasswordEntry
        fields = ['website', 'category', 'password']