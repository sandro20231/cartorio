from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.logina, name='login'),
    path('logout/', views.logouta, name='logout'),
    path("novoregistro/", views.novoregistro, name="novoregistro"),
    path('listarregistros/', views.listarregistros, name="listarregistros"),
    
]
