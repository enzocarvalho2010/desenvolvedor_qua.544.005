class Pessoa:
    def __init__(self,email,telefone):
        self.__email = email
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone

class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,telefone,email):
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(email=email,telefone=telefone)

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self,razao,cnpj,fantasia,email,telefone):
        self.__razao = razao
        self.__fantasia = fantasia
        self.__cnpj = cnpj
        super().__init__(email, telefone)

    @property
    def razao(self):
        return self.__razao
    @razao.setter
    def razao(self,razao):
        self.__razao = razao

    @property
    def fantasia(self):
        return self.__fantasia
    @fantasia.setter
    def fantasia(self,fantasia):
        self.__fantasia = fantasia

    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self,cnpj):
        self.__cnpj = cnpj
# SIX SEVEEN