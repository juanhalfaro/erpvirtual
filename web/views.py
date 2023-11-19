from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import Register ,LoginForm
from .models import Usuario
from django.conf import settings

# Create your views here.

def inicio(request):
    
    context={}
    return render(request, "inicio.html", context)


def registro(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
                # Obtén los datos del formulario
                email = form.cleaned_data['Email']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # Crea una instancia de Usuario y guárdala en la base de datos
                usuario = Usuario(Email=email, username=username, password=password)
                usuario.save()

                # Redirecciona a una página de éxito o realiza otras acciones necesarias
                return redirect('web:login')  # Cambia 'pagina_de_exito' por la URL a la que quieras redirigir
    else:
        form = Register()
    
    context = {
        'form': form,
        }
    return render(request, "registro.html", context)




def login(request):
    # if request.user.is_authenticated:
    #     return redirect('web:dashboard')
    
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         usuario = authenticate(username=username, password=password)
    #         if usuario is not None:
    #             auth_login(request, usuario)
    #             if 'next' in request.GET:
    #                 return redirect(request.GET['next'])
    #             return redirect("web:dashboard")
    #         else:
    #             error_message = "Por favor introduzca un nombre de usuario y contraseña correctos."
    #             messages.error(request, error_message)
    #             print("valio verga sherk", error_message)
    # else:
    #     form = LoginForm() 

    context = {
        # 'form': form,
    }
    return render(request, "registration/login.html", context)








# @login_required
def dashboard(request):


    context={
        
    }
    return render(request, "dashboard.html", context)