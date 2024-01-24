from django import forms
from .models import Pedidos
from django.contrib.auth.forms import UserCreationForm


class Register(forms.Form):
    RazonS = forms.CharField()
    DireccionF = forms.CharField()
    CodigoP = forms.CharField()
    RFC = forms.CharField()
    DireccionE = forms.CharField()
    Email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
               
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
        


class Pedido(forms.Form):
    Moneda = forms.CharField()
    Solicitante = forms.CharField()
    Empresa = forms.CharField()
    Direccion = forms.CharField()
    Telefono = forms.CharField()
    Cantidad = forms.CharField()
    Detalles = forms.CharField()
    

