import os
from model import PessoaFisica,PessoaJuridica

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # instancia a classe
    user = PessoaFisica(nome='',cpf='',email='',telefone='')
    emp = PessoaJuridica(razao='',fantasia='',cnpj='',email='',telefone='')

    li()
    print(f'{'-'*20} Insira os dados do usuário {'-'*20}')
    user.nome = input('Nome: ').strip().title()
    user.cpf = input('CPF: ').strip()
    user.email = input('Email: ').strip().lower()
    user.telefone = input('Telefone: ').strip()

    li()
    print(f'{'-'*20} Insira os dados da empresa {'-'*20}')
    emp.razao = input('Razão Social: ').strip()
    emp.fantasia = input('Nome: ').strip().title()
    emp.cnpj = input('CNPJ: ').strip()
    emp.email = input('Email: ').strip().lower()
    emp.telefone = input('Telefone: ').strip()

    li()
    print(f'{'-'*20} DADOS DO USUÁRIO {'-'*20}')
    print(f'Nome: {user.nome}')
    print(f'CPF: {user.cpf}')
    print(f'Email: {user.email}')
    print(f'Telefone: {user.telefone}')

    print(f'{'-'*20} DADOS DA EMPRESA {'-'*20}')
    print(f'Razão Social: {emp.razao}')
    print(f'Nome: {emp.fantasia}')
    print(f'CNPJ: {emp.cnpj}')
    print(f'Email: {emp.email}')
    print(f'Telefone: {emp.telefone}')

if __name__ == '__main__':
    main()