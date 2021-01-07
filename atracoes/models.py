from django.db import models
from django.db.models import IntegerField
from django.db.models import ImageField


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    horario_func = models.TextField()
    idade_min: IntegerField = models.IntegerField()
    foto: ImageField = models.ImageField(upload_to='atracoes', null=True, blank=True)

    def __str__(self):
        return self.nome
