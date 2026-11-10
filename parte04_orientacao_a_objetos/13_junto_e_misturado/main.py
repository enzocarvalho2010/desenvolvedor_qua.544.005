import os
import random
from model import Pessoa ,ContaCorrente , ContaPoupanca

def li():
    os.system('cls' if os.name == 'nt' else 'clear')
#TODO terminar função operacoes()
def operacoes(agencia,conta,user):
    if conta == '1':
        conta = ContaCorrente(agencia=agencia
                              ,numero=f'{random.randint(10000,99999)}-1'
                              ,saldo=0.0
                              ,titular=user
                              ,taxa=0.01)
    else:
        conta = ContaPoupanca(agencia=agencia
                              ,numero=f'{random.randint(10000,99999)}-2'
                              ,saldo=0.0
                              ,titular=user
                              ,juros=0.01)
    while True:
        print('0. Sair do pogramia')
        print('1. Consultar dados')
        print('2. Depositar dinheiro')
        print('3. sacar dinheiro')
        op = input('Operação desejada: ').strip()
        match op:
            case '0':
                print('Pogramia encerrado.')
                break
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case _:
                print('Opção inválida :(')
                continue

def main():
    user = Pessoa(nome='',cpf='')
    li()
    user.nome = input('Insira o nome: ').strip().title()
    user.cpf = input('Insira o CPF: ').strip()
    li()
    print('1. Conta corrente')
    print('2. Conta poupança')
    conta = input('Escolha a conta que deseja criar: ').strip()
    li()
    if conta == '1' or conta == '2':
        operacoes('1234-1',conta,user)
    else:
        print('Tipo de conta inválida :(')

if __name__== '__main__':
    main()