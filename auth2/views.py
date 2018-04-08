from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from django.contrib.auth import authenticate, login as login_mio, logout as logout_mio
from django.contrib.auth.models import User



# Create your views here.
def login(request):
    titulo 	= 'Login'
    template = loader.get_template('auth2/login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_mio(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Error en password o usuario')
    context = {
    'titulo': titulo,
    }
    return HttpResponse(template.render(context, request))


def register(request):
    titulo 	= 'Register'
    template = loader.get_template('auth2/register.html')
    if request.method == "POST":
        username 	= request.POST['username']
        email 		= request.POST['email']
        password 	= request.POST['password']
                
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is None:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, 'Registro completo, ahora puede loguearse.')
            return redirect('login')
        else:
            messages.error(request, 'Nombre de usuario duplicado.')

    context = {
        'titulo': titulo,
    }

    return HttpResponse(template.render(context, request))



def logout(request):
    logout_mio(request)
    return redirect('login')