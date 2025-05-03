from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Registro, Transmissaodebens

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


def novoregistro(request):
    if request.method == "POST":
        dataCriacao = request.POST['dataregistro']
        descricao = request.POST['descricaonovoregistro']
        contribuinte = request.POST['contribuinte']
        proprietario = request.POST['proprietario']
        cpf = request.POST['cpfproprietario']
        registroanterior = request.POST['registroanterior']

        insert = Registro(datacriacao=dataCriacao, localizacao=descricao, contribuinte=contribuinte,
                          proprietario=proprietario, registro_anterior=registroanterior, cpf_proprietario=cpf, ativo=True)
        insert.save()
        return HttpResponseRedirect(reverse('listarregistros'))

    return render(request, "registro/novoregistro.html")


def listarregistros(request):
    return render(request, 'registro/listarregistros.html', {"registros": Registro.objects.all()})


def mostrarmatricula(request, matricula):
    dados = Registro.objects.get(pk=matricula)
    transmissoes = Transmissaodebens.objects.filter(matricula=matricula)
    return render(request, "registro/matricula.html", {"dado": dados, "ts": transmissoes})


def buscarmatricula(request):
    matricula = request.POST.get('buscamatricula')
    dados = Registro.objects.get(pk=matricula)
    transmissoes = Transmissaodebens.objects.filter(matricula=matricula)
    return render(request, "registro/matricula.html", {"dado": dados, "ts": transmissoes})


def buscadocumento(request):
    documento = request.POST.get('buscadocumento')
    dados = Registro.objects.filter(cpf_proprietario=documento)
    return render(request, "registro/listapordocumento.html", {"registros": dados})


def transmitir(request):
    if request.method == "POST":
        datatransmissao = request.POST['datatransmissao']
        matricula = request.POST['matriculatransmitida']
        comprador = request.POST['compradordebens']
        documento = request.POST['cpfcompradordebens']
        vendedor = request.POST['vendedordebens']
        documentoVendedor = request.POST['cpfvendedordebens']
        valor = request.POST['valordetransmissao']

        imovel = Registro.objects.get(pk=matricula)
        imovel.proprietario = comprador
        imovel.cpf_proprietario = documento
        imovel.save()

        registro = Transmissaodebens(
            dataTransmissao=datatransmissao, matricula=imovel, nomeComprador=comprador, cpfComprador=documento, valor=valor, nomeVendedor=vendedor, cpfVendedor=documentoVendedor)
        registro.save()
        return HttpResponseRedirect(reverse('listarregistros'))

    return render(request, "registro/transmissao.html")
