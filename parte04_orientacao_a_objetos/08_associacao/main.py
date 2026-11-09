import os
from model import Pessoa,Endereco

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    endereco = Endereco(cep='',uf='',cidade='',bairro='',lo='',comp='',num='')
    user = Pessoa(nome='',cpf='',email='',telefone='',endereco=endereco)
    li()

    user.nome = input('Insira o nome: ').strip().title()
    user.cpf = input('Insira o CPF: ').strip()
    user.email = input('Insira o email: ').strip().lower()
    user.telefone = input('Insira o telefone: ').strip()
    endereco.cep = input('Insira o CEP: ').strip()
    endereco.uf = input('Insira a UF: ').strip().upper()
    endereco.cidade = input('Insira a cidade: ').strip().title()
    endereco.bairro = input('Insira o bairro: ').strip().title()
    endereco.lo = input('Insira o logradouro: ').strip()
    endereco.comp = input('Insira o complemento: ')
    endereco.num = input('Insira o número: ').strip()

    user.exibir()

if __name__ == "__main__":
    main()