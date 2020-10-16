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

class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome da instituicao')

    def __str__(self):
        return self.nome_instituicao

class Curso(models.Model):
    nome_curso = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome do curso')

    def __str__(self):
        return self.nome_curso
