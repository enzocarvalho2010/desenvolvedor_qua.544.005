# superclasse / classe-pai
class Pessoa:
    def __init__(self,email,telefone,endereco):
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
    # método da classe
    def exibir(self):
        print(f'Email: {self.email}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')

# subclasses / classes-filhas
class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,email,telefone,endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(email=email,telefone=telefone,endereco=endereco)
    
    def exibir(self):
        print(f'{'-'*20} DADOS DO USUÁRIO {'-'*20}')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        super().exibir()

class PessoaJuridica(Pessoa):
    def __init__(self,email,endereco,telefone,cnpj,razao_social,nome_fantasia):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.razao_social = razao_social
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir(self):
        print(f'{'-'*20} DADOS DA EMPRESA {'-'*20}')
        print(f'Razão Social: {self.razao_social}')
        print(f'Nome: {self.nome_fantasia}')
        print(f'CNPJ: {self.cnpj}')
        super().exibir()