# importa abstração
from abc import ABC, abstractmethod

# interface / classe abstrata
class IConta(ABC):
    @abstractmethod
    def consultar(self):
        pass

    @abstractmethod
    def depositar(self,valor):
        pass
    
    @abstractmethod
    def sacar(self,valor):
        pass

# classe Conta
class Conta(IConta):
    def __init__(self,titular,cpf,agencia,numero,saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self,agencia):
        self.__agencia = agencia
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,numero):
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    # métodos da interface
    def consultar(self):
        print(f'{'-'*20} Dados da conta {'-'*20}')
        print(f'Nome do titular: {self.__titular}')
        print(f'CPF do titular: {self.__cpf}')
        print(f'Agência: {self.__agencia}')
        print(f'Conta: {self.__numero}')
        print(f'Saldo: {self.__saldo:.2f} R$')

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def sacar(self, valor):
        self.__saldo += valor
        return self.__saldo