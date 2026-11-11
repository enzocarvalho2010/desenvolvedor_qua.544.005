import os
import random
from model import Pessoa ,ContaCorrente , ContaPoupanca

def li():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def operacoes(agencia,conta,user):
    if conta == '1':
        conta = ContaCorrente(agencia=agencia
                              ,numero=f'{random.randint(10000,99999)}-1'
                              ,tipo='Conta Corrente'
                              ,saldo=0.0
                              ,titular=user
                              ,taxa=0.01)
    else:
        conta = ContaPoupanca(agencia=agencia
                              ,numero=f'{random.randint(10000,99999)}-2'
                              ,tipo='Conta Poupança'
                              ,saldo=0.0
                              ,titular=user
                              ,juros=0.1)
    while True:
        print('0. Sair do pogramia')
        print('1. Consultar dados')
        print('2. Depositar dinheiro')
        print('3. Sacar dinheiro')
        op = input('Operação desejada: ').strip()
        match op:
            case '0':
                print('Pogramia encerrado.')
                break
            case '1':
                conta.consultar()
                continue
            case '2':
                valor = float(input('Insira o valor do depósito: ').replace(',','.'))
                saldo = conta.depositar(valor)
                li()
                print(f'Depósito concluído! Saldo atual: {saldo:.2f}')
                continue
            case '3':
                valor = float(input('Insira o valor que deseja sacar: ').replace(',','.'))
                if valor < conta.saldo:
                    saldo = conta.sacar(valor)
                    li()
                    print(f'Saque concluído! Saldo atual: {saldo:.2f}')
                else:
                    print('Saque não perimitido :(')
                continue
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