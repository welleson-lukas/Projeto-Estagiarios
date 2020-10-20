from ..models import Estagiario


def listar_estagiario_id(id):
    return Estagiario.objects.get(id=id)


def editar_estagiario(estagiario_bd, estagiario_novo):
    estagiario_bd.nome = estagiario_novo.nome
    estagiario_bd.email = estagiario_novo.email
    estagiario_bd.telefone = estagiario_novo.telefone
    estagiario_bd.dt_nascimento = estagiario_novo.dt_nascimento
    estagiario_bd.status = estagiario_novo.status
    estagiario_bd.contrato = estagiario_novo.contrato
    estagiario_bd.documento = estagiario_novo.documento
    estagiario_bd.n_contrato = estagiario_novo.n_contrato
    estagiario_bd.inicio_contrato = estagiario_novo.inicio_contrato
    estagiario_bd.fim_contrato = estagiario_novo.fim_contrato
    estagiario_bd.instituicao_edu = estagiario_novo.instituicao_edu
    estagiario_bd.curso = estagiario_novo.curso
    estagiario_bd.save(force_update=True)

