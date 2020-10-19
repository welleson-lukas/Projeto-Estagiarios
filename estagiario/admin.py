from django.contrib import admin

from .models import Estagiario, Contrato

class ContratoInLine(admin.TabularInline):
    model = Contrato
    extra = 1

class EstagiarioAdmin(admin.ModelAdmin):

    inlines = [
        ContratoInLine
    ]

admin.site.register(Estagiario, EstagiarioAdmin)
admin.site.register(Contrato)
