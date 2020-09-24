from django.db import models
from django.utils import timezone
from core.models import *

class Estagiario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nome completo')
    email = models.EmailField(null=False, blank=False, verbose_name='Email')
    telefone = models.CharField(max_length=100, null=False, blank=True, verbose_name='Telefone')
    dt_nascimento = models.DateField(null=False, blank=False, verbose_name='Data de nascimento')
    orgao = models.ForeignKey(Orgao, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Orgão')
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Setor')
    dt_cadastro = models.DateField(default=timezone.now, blank=False, null=False, verbose_name='Data de cadastro')
    status = models.BooleanField(default=False, verbose_name='Ativo')
    contrato = models.TextField(blank=False, null=False, verbose_name='Descrição do contrato')
    n_contrato = models.IntegerField(blank=False, null=True, verbose_name='Número do contrato')
    inicio_contrato = models.DateField(blank=False, null=False, verbose_name='Data de inicio')
    fim_contrato = models.DateField(blank=False, null=False, verbose_name='Data de término')
    instituicao_edu = models.CharField(max_length=200, blank=False, null=False, verbose_name='Instituição de ensino')
    curso = models.CharField(max_length=200, blank=False, null=True, verbose_name='Curso')

    def __str__(self):
        return self.nome