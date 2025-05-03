from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='teste'),
    path('', views.login, name='login')
]
