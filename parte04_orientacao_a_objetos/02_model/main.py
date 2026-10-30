import os
from model import Pessoa

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    li()

    user = Pessoa(nome='',idade=0,email='')

    user.nome = input('Informe o nome: ').strip().title()
    user.idade = int(input('Informe a idade: '))
    user.email = input('Informe o email: ').strip().lower()

    user.cumprimentar()

if __name__ == '__main__':
    main()