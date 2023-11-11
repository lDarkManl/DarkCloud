from django.contrib.auth.forms import AuthenticationForm
from django import forms

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'Имя пользователя'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'Пароль'}))