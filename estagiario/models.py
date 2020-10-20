from django.db import models
from django.utils import timezone
from core.models import *


class Estagiario(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nome completo')
    cpf = models.CharField(max_length=14, null=True, blank=True, verbose_name='CPF')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    telefone = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telefone')
    dt_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de nascimento')
    orgao = models.ForeignKey(Orgao, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Orgão')
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Setor')
    dt_cadastro = models.DateField(default=timezone.now, blank=True, null=True, verbose_name='Data de cadastro')
    status = models.BooleanField(default=False, verbose_name='Ativo')
    instituicao_edu = models.ForeignKey(Instituicao, on_delete=models.DO_NOTHING, max_length=200, blank=True, null=True, verbose_name='Instituição de ensino')
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, max_length=200, blank=True, null=True, verbose_name='Curso')
    contrato = models.TextField(blank=True, null=True, verbose_name='Descrição do contrato')
    n_contrato = models.CharField(max_length=15, blank=True, null=True, verbose_name='Número do contrato')
    inicio_contrato = models.DateField(blank=True, null=True, verbose_name='Data de inicio')
    fim_contrato = models.DateField(blank=True, null=True, verbose_name='Data de término')
    documento = models.FileField(upload_to='media', null=True, verbose_name='Documento')

    #TODO ajustar 'blank e null'

    def __str__(self):
        return self.nome
