class Estagiario():
    def __init__(self, nome, email, telefone, dt_nascimento, orgao, setor, dt_cadastro, status, contrato, documento,
                 n_contrato, inicio_contrato, fim_contrato, instituicao, curso):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__dt_nascimento = dt_nascimento
        self.__orgao = orgao
        self.__setor = setor
        self.__dt_cadastro = dt_cadastro
        self.__status = status
        self.__contrato = contrato
        self.__documento = documento
        self.__n_contrato = n_contrato
        self.__inicio_contrato = inicio_contrato
        self.__fim_contrato = fim_contrato
        self.__instituicao = instituicao
        self.__curso = curso

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    #######################

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
    #######################

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    #######################

    @property
    def dt_nascimento(self):
        return self.__dt_nascimento

    @dt_nascimento.setter
    def dt_nascimento(self, dt_nascimento):
        self.__dt_nascimento = dt_nascimento

    #######################

    @property
    def orgao(self):
        return self.__orgao

    @orgao.setter
    def orgao(self, orgao):
        self.__orgao = orgao

    #######################

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    #######################

    @property
    def dt_cadastro(self):
        return self.__dt_cadastro

    @dt_cadastro.setter
    def dt_cadastro(self, dt_cadastro):
        self.__dt_cadastro = dt_cadastro

    #######################

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    #######################

    @property
    def contrato(self):
        return self.__contrato

    @contrato.setter
    def contrato(self, contrato):
        self.__contrato = contrato

    #######################

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, documento):
        self.__documento = documento

    #######################

    @property
    def n_contrato(self):
        return self.__n_contrato

    @n_contrato.setter
    def n_contrato(self, n_contrato):
        self.__n_contrato = n_contrato

    #######################

    @property
    def inicio_contrato(self):
        return self.__inicio_contrato

    @inicio_contrato.setter
    def inicio_contrato(self, inicio_contrato):
        self.__inicio_contrato = inicio_contrato

    #######################

    @property
    def fim_contrato(self):
        return self.__fim_contrato

    @fim_contrato.setter
    def fim_contrato(self, fim_contrato):
        self.__fim_contrato = fim_contrato

    #######################

    @property
    def instituicao(self):
        return self.__instituicao

    @instituicao.setter
    def instituicao(self, instituicao):
        self.__instituicao = instituicao

    #######################

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    #######################