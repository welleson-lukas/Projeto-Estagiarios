from django.contrib import admin
from .models import Orgao, Setor, Instituicao, Curso

admin.site.register(Orgao)
admin.site.register(Setor)
admin.site.register(Instituicao)
admin.site.register(Curso)