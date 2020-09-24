from django.db import models
from django.utils import timezone

class Orgao(models.Model):
    nome_orgao = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome do orgão')

    def __str__(self):
        return self.nome_orgao


class Setor(models.Model):
    nome_setor = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome do setor')

    def __str__(self):
        return self.nome_setor
