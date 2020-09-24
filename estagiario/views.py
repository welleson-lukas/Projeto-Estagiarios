from django.shortcuts import render, redirect
from django.http import HttpResponse
from estagiario.models import Estagiario
from .entidades import estagiario
from .services import estagiario_service
from .forms import EstagiarioForm

def index(request):
    estagiarios = Estagiario.objects.all()
    return render(request, 'estagiario/index.html', {'estagiarios': estagiarios})

def alertacontrato(request):
    contrato_estagio = Estagiario.objects.all()
    return render(request, 'estagiario/index.html', {'contrato_estagio': contrato_estagio})

def cadastrar_estagiario(request):
    if request.method == "POST":
        form_estagiario = EstagiarioForm(request.POST)
        if form_estagiario.is_valid():
            nome = form_estagiario.cleaned_data["nome"]
            email = form_estagiario.cleaned_data["email"]
            telefone = form_estagiario.cleaned_data["telefone"]
            dt_nascimento = form_estagiario.cleaned_data["dt_nascimento"]
            orgao = form_estagiario.cleaned_data["orgao"]
            setor = form_estagiario.cleaned_data["setor"]
            status = form_estagiario.cleaned_data["status"]
            contrato = form_estagiario.cleaned_data["contrato"]
            n_contrato = form_estagiario.cleaned_data["n_contrato"]
            inicio_contrato = form_estagiario.cleaned_data["inicio_contrato"]
            fim_contrato = form_estagiario.cleaned_data["fim_contrato"]
            instituicao_edu = form_estagiario.cleaned_data["instituicao_edu"]
            curso = form_estagiario.cleaned_data["curso"]

            estagiario_novo = Estagiario(nome=nome, email=email, telefone=telefone, dt_nascimento=dt_nascimento,
                                         orgao=orgao, setor=setor, status=status, contrato=contrato,
                                         n_contrato=n_contrato, inicio_contrato=inicio_contrato, fim_contrato=fim_contrato,
                                         instituicao_edu=instituicao_edu, curso=curso)

            estagiario_service.cadastrar_estagiario(estagiario_novo)
            return redirect('index')
    else:
        form_estagiario = EstagiarioForm()
    return render(request, 'estagiario/form_estagiario.html', {"form_estagiario": form_estagiario})

def editar_estagiario(request, id):
    estagiario_bd = estagiario_service.listar_estagiario_id(id)
    form_estagiario = EstagiarioForm(request.POST or None, instance=estagiario_bd)
    if form_estagiario.is_valid():
        nome = form_estagiario.cleaned_data["nome"]
        email = form_estagiario.cleaned_data["email"]
        telefone = form_estagiario.cleaned_data["telefone"]
        dt_nascimento = form_estagiario.cleaned_data["dt_nascimento"]
        orgao = form_estagiario.cleaned_data["orgao"]
        setor = form_estagiario.cleaned_data["setor"]
        status = form_estagiario.cleaned_data["status"]
        contrato = form_estagiario.cleaned_data["contrato"]
        n_contrato = form_estagiario.cleaned_data["n_contrato"]
        inicio_contrato = form_estagiario.cleaned_data["inicio_contrato"]
        fim_contrato = form_estagiario.cleaned_data["fim_contrato"]
        instituicao_edu = form_estagiario.cleaned_data["instituicao_edu"]
        curso = form_estagiario.cleaned_data["curso"]

        estagiario_novo = Estagiario(nome=nome, email=email, telefone=telefone, dt_nascimento=dt_nascimento,
                                     orgao=orgao, setor=setor, status=status, contrato=contrato,
                                     n_contrato=n_contrato, inicio_contrato=inicio_contrato, fim_contrato=fim_contrato,
                                     instituicao_edu=instituicao_edu, curso=curso)
        estagiario_service.editar_estagiario(estagiario_bd, estagiario_novo)
        return redirect('index')
    return render(request, 'estagiario/form_estagiario.html', {"form_estagiario": form_estagiario})



def exibir_estagiario(request, estagiario_id):
    estagiario = Estagiario.objects.get(id=estagiario_id)
    return render(request, 'estagiario/detalhes_estagiario.html', {'estagiario': estagiario})