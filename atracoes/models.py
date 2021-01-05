from django.db import models
from django.db.models import IntegerField


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    horario_func = models.TextField()
    idade_min: IntegerField = models.IntegerField()

    def __str__(self):
        return self.nome
