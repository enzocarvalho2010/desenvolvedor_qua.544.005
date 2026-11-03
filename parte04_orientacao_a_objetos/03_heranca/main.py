import os
from model import PessoaFisica, PessoaJuridica

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    user = PessoaFisica(nome='',cpf='',email='',endereco='',telefone='')
    emp = PessoaJuridica(cnpj='',razao_social='',nome_fantasia='',email='',endereco='',telefone='')
    # informa os dados do usuário
    li()
    print(f'{'-'*20} Insira os dados do usuário {'-'*20}\n')
    user.nome = input('Nome: ').strip().title()
    user.cpf = input('CPF: ').strip()
    user.email = input('Email: ').strip().lower()
    user.telefone = input('Telefone: ').strip()
    user.endereco = input('Endereço: ').strip()

    # informa os dados da empresa
    li()
    print(f'{'-'*20} Insira os dados do usuário {'-'*20}\n')
    emp.razao_social = input('Razão Social: ').strip()
    emp.nome_fantasia = input('Nome: ').strip()
    emp.cnpj = input('CNPJ: ').strip().lower()
    emp.email = input('Email: ').strip().lower()
    emp.telefone = input('Telefone: ').strip()
    emp.endereco = input('Endereço: ').strip()

    # exibe os dados
    li()
    user.exibir()
    emp.exibir()

if __name__ == '__main__':
    main()