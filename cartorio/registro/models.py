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
