from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        HttpResponseRedirect(reverse('index'))
    return render(request, 'registro/login.html')


def login(request):
    return render(request, 'registro/login.html')
