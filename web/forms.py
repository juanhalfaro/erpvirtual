from django import forms
from django.contrib.auth.forms import UserCreationForm


class Register(forms.Form):
    Email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
        
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
        

