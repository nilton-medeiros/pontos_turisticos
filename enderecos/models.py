from django.db import models
from django.db.models import CharField, IntegerField


class Endereco(models.Model):
    logradouro: CharField = models.CharField(max_length=150)
    complemento: CharField = models.CharField(max_length=150)
    cidade: CharField = models.CharField(max_length=100)
    estado: CharField = models.CharField(max_length=50)
    pais: CharField = models.CharField(max_length=70)
    latitude: IntegerField = models.IntegerField(null=True, blank=True)
    longitude: IntegerField = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.logradouro
