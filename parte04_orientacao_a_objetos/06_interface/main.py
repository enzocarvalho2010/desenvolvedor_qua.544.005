import os
import random
from model import Conta

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # instancia a classe Conta
    cc = Conta(titular='',cpf='',agencia='1010-1',numero=f'{random.randint(10000,99999)}-1',saldo=0.0)

    li()
    cc.titular = input('Insira o nome: ').strip().title()
    cc.cpf = input('Insira o CPF: ').strip()

    li()
    while True:
        # menu
        print(f'{'-'*20} COBRANK {'-'*20}')
        print('0. Encerrar programa')
        print('1. Exibir dados da conta')
        print('2. Despositar dinheiro')
        print('3. Sacar dinheiro')
        op = input('Digite a opção desejada: ').strip()
        li()

        match op:
            case '0':
                print('Programa encerrado.')
                break
            case '1':
                cc.consultar() 
                continue
            case '2':
                valor = float(input('Digite o valor do depósito: R$').replace(',','.'))
                saldo = cc.depositar(valor)
                li()
                print(f'Depósito efetuado com sucesso! Saldo: {saldo:.2f}R$ ')
                continue
            case '3':
                valor = float(input('Digite o valor do saque: R$').replace(',','.'))
                if valor <= cc.saldo:
                    saldo = cc.sacar(valor)
                    li()
                    print(f'Saque efetuado com sucesso! Saldo: {cc.saldo:.2f}R$ ')
                else:
                    print('Não foi possível efetuar o saque :(')
                continue
            case _:
                print('Opção inválida :(')
                continue

if __name__ == '__main__':
    main()