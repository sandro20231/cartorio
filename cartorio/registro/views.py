from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'registro/index.html')
    return render(request, 'registro/login.html')


def logina(request):
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['senha']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'registro/login.html', {"mensagemerro": "Usuário ou senha inválidos"})
    return render(request, 'registro/login.html')


def logouta(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
