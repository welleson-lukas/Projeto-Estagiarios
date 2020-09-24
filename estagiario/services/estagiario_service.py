from ..models import Estagiario

def cadastrar_estagiario(estagiario):
    Estagiario.objects.create(nome=estagiario.nome, email=estagiario.email, telefone=estagiario.telefone, dt_nascimento=estagiario.dt_nascimento,
                              orgao=estagiario.orgao, setor=estagiario.setor, dt_cadastro=estagiario.dt_cadastro, status=estagiario.status,
                              contrato=estagiario.contrato, n_contrato=estagiario.n_contrato, inicio_contrato=estagiario.inicio_contrato,
                              fim_contrato=estagiario.fim_contrato, instituicao_edu=estagiario.instituicao_edu, curso=estagiario.curso)

def listar_estagiario_id(id):
    return Estagiario.objects.get(id=id)


def editar_estagiario(estagiario_bd, estagiario_novo):
    estagiario_bd.nome = estagiario_novo.nome
    estagiario_bd.email = estagiario_novo.email
    estagiario_bd.telefone = estagiario_novo.telefone
    estagiario_bd.dt_nascimento = estagiario_novo.dt_nascimento
    estagiario_bd.status = estagiario_novo.status
    estagiario_bd.contrato = estagiario_novo.contrato
    estagiario_bd.n_contrato = estagiario_novo.n_contrato
    estagiario_bd.inicio_contrato = estagiario_novo.inicio_contrato
    estagiario_bd.fim_contrato = estagiario_novo.fim_contrato
    estagiario_bd.instituicao_edu = estagiario_novo.instituicao_edu
    estagiario_bd.curso = estagiario_novo.curso
    estagiario_bd.save(force_update=True)

