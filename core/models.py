from django.db import models
from django.utils import timezone

class Orgao(models.Model):
    nome_orgao = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nome do orgão')

    def __str__(self):
        return self.nome_orgao


class Setor(models.Model):
    nome_setor = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nome do setor')
    orgao = models.ForeignKey(Orgao, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nome_setor


class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nome da IES')

    def __str__(self):
        return self.nome_instituicao


class Curso(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome_curso = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nome do setor')

    def __str__(self):
        return self.nome_curso