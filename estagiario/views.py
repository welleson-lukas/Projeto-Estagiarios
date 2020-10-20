from datetime import date, timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from estagiario.models import Estagiario
from django.db.models import Q, Count, Case, When
from .services import estagiario_service
from .forms import EstagiarioForm


class EstagiarioIndex(ListView):
    model = Estagiario
    template_name = 'estagiario/index.html'
    context_object_name = 'estagiarios'

    def get_queryset(self):

        data_limite = date.today() + timedelta(days=20)
        data_atual = date.today()

        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(status=True)
        qs = qs.annotate(
            numero_contratos=Count(
                Case(
                    When(
                        fim_contrato__gt=data_atual, fim_contrato__lt=data_limite, then=1
                    )
                )
            )
        )

        messages.warning(self.request, 'Comentário enviado com sucesso')

        return qs

class EstagiarioInativos(ListView):
    model = Estagiario
    template_name = 'estagiario/inativos.html'
    context_object_name = 'estagiarios'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(status=False)

        return qs


def cadastrar_estagiario(request):
    if request.method == "POST":
        form_estagiario = EstagiarioForm(request.POST, request.FILES)

        if form_estagiario.is_valid():
            form_estagiario.save()
            return redirect('index')

    else:
        form_estagiario = EstagiarioForm()
    return render(request, 'estagiario/form_estagiario.html', {"form_estagiario": form_estagiario})

def editar_estagiario(request, id):
    estagiario_bd = estagiario_service.listar_estagiario_id(id)
    form_estagiario = EstagiarioForm(request.POST or None, request.FILES or None, instance=estagiario_bd)
    if form_estagiario.is_valid():
        nome = form_estagiario.cleaned_data["nome"]
        email = form_estagiario.cleaned_data["email"]
        telefone = form_estagiario.cleaned_data["telefone"]
        dt_nascimento = form_estagiario.cleaned_data["dt_nascimento"]
        orgao = form_estagiario.cleaned_data["orgao"]
        setor = form_estagiario.cleaned_data["setor"]
        status = form_estagiario.cleaned_data["status"]
        contrato = form_estagiario.cleaned_data["contrato"]
        documento = form_estagiario.cleaned_data["documento"]
        n_contrato = form_estagiario.cleaned_data["n_contrato"]
        inicio_contrato = form_estagiario.cleaned_data["inicio_contrato"]
        fim_contrato = form_estagiario.cleaned_data["fim_contrato"]
        instituicao_edu = form_estagiario.cleaned_data["instituicao_edu"]
        curso = form_estagiario.cleaned_data["curso"]

        estagiario_novo = Estagiario(nome=nome, email=email, telefone=telefone, dt_nascimento=dt_nascimento,
                                     orgao=orgao, setor=setor, status=status, contrato=contrato, documento=documento,
                                     n_contrato=n_contrato, inicio_contrato=inicio_contrato, fim_contrato=fim_contrato,
                                     instituicao_edu=instituicao_edu, curso=curso)
        estagiario_service.editar_estagiario(estagiario_bd, estagiario_novo)
        return redirect('index')
    return render(request, 'estagiario/form_estagiario.html', {"form_estagiario": form_estagiario})



def exibir_estagiario(request, estagiario_id):
    estagiario = Estagiario.objects.get(id=estagiario_id)
    return render(request, 'estagiario/detalhes_estagiario.html', {'estagiario': estagiario})

