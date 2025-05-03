from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.logina, name='login'),
    path('logout/', views.logouta, name='logout'),
    path("novoregistro/", views.novoregistro, name="novoregistro"),
    path('listarregistros/', views.listarregistros, name="listarregistros"),
    path('id/<int:matricula>', views.mostrarmatricula, name="mostrarmatricula"),
    path('listarregistros/<int:matricula>',
         views.mostrarmatricula, name="mostrarmatricula2"),
    path('buscarmatricula/', views.buscarmatricula, name='buscarmatricula'),
    path('buscadocumento', views.buscadocumento, name="buscadocumento"),
    path('<int:matricula>', views.mostrarmatricula, name='mostrarmatricula3')


]
