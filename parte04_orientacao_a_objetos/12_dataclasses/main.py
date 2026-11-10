import os
from model import Pessoa

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    li()
    user = Pessoa(nome='',cpf='',email='',idade=0,altura=0.0)
    user.nome = input('Digite o nome: ').strip().title()
    user.cpf = input('Digite o CPF: ').strip
    user.email = input('Digite o email: ').strip().lower()
    user.idade = int(input('Digite a idade: '))
    user.altura = float(input('Digite a idade: ').replace(',','.'))
    
    li()
    print(f'Nome: {user.nome}')
    print(f'CPF: {user.cpf}')
    print(f'Email: {user.email}')
    print(f'Idade: {user.idade}')
    print(f'Altura: {user.altura}')

if __name__ == '__main__':
    main()