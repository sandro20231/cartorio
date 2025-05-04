from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import RegistroViewSet, TransmissaoDeBensViewSet
router = DefaultRouter()
router.register(r'registros', RegistroViewSet)
router.register(r'transmissoes', TransmissaoDeBensViewSet)
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
    path('<int:matricula>', views.mostrarmatricula, name='mostrarmatricula3'),
    path('transmitirbens', views.transmitir, name='transmitir'),
    path('desdobro', views.desdobro, name="desdobro"),
    path('api/', include(router.urls)),  # A URL base da API será /api/


]
