from django.db import models

# Create your models here.


class Registro(models.Model):
    datacriacao = models.DateField()
    localizacao = models.CharField(max_length=10000)
    contribuinte = models.IntegerField()
    registro_anterior = models.IntegerField()
    proprietario = models.CharField(max_length=100)
    cpf_proprietario = models.IntegerField()
    ativo = models.BooleanField()

    def __str__(self):
        return f"{self.id} - {self.contribuinte} - {self.proprietario}"


class Transmissaodebens(models.Model):
    dataTransmissao = models.DateField()
    matricula = models.ForeignKey(
        Registro, on_delete=models.CASCADE, related_name="matriculadetransmissao")
    nomeComprador = models.CharField(max_length=100)
    nomeVendedor = models.CharField(max_length=100, default='a')
    cpfVendedor = models.CharField(max_length=100, default='1000000')
    cpfComprador = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.id} - {self.matricula} - {self.nomeComprador} - {self.valor}"
