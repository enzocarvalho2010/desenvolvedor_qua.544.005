import os
from model import Pessoa

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    li()
    user = Pessoa(nome='',idade=0,altura=0.0)
    user.nome = input('Digite o nome: ').strip().title()
    user.idade = int(input('Digite a idade: '))
    user.altura = float(input('Digite a altura em metros: ').replace(',','.'))
    li()
    print(user)
    del(user)

if __name__ == '__main__':
    main()