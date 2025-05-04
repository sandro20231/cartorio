# serializers.py

from rest_framework import serializers
from .models import Registro, Transmissaodebens


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'


class TransmissaoDeBensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmissaodebens
        fields = '__all__'
