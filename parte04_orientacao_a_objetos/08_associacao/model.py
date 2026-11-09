class Endereco:
    def __init__(self,cep,uf,cidade,bairro,lo,comp,num):
        self.__cep = cep
        self.__uf = uf
        self.__cidade = cidade
        self.__bairro = bairro
        self.__lo = lo
        self.__comp = comp
        self.__num = num

    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self,cep):
        self.__cep = cep

    @property
    def uf(self):
        return self.__uf
    @uf.setter
    def uf(self,uf):
        self.__uf = uf

    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self,cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self,bairro):
        self.__bairro = bairro

    @property
    def lo(self):
        return self.__lo
    @lo.setter
    def lo(self,lo):
        self.__lo = lo

    @property
    def comp(self):
        return self.__comp
    @comp.setter
    def comp(self,comp):
        self.__comp = comp

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self,num):
        self.__num = num

    def obter(self):
        return f'CEP: {self.__cep}\nUF: {self.__uf}\nCidade: {self.__cidade}\nBairro: {self.__bairro}\nLogradouro: {self.__lo}\nComplemeto: {self.__comp}\nNúmero: {self.__num}\n'

class Pessoa:
    def __init__(self,nome,cpf,email,telefone,endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco

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

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self,endereco):
        self.__endereco = endereco

    def exibir(self):
        print(f'Nome: {self.__nome}')
        print(f'CPF: {self.__cpf}')
        print(f'Email: {self.__email}')
        print(f'Telefone: {self.__telefone}')
        print(f'Endereço: {self.__endereco.obter()}')