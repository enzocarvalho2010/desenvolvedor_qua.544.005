from abc import ABC,abstractmethod
from dataclasses import dataclass

# interface
class IConta(ABC):
    @abstractmethod
    def consultar(self):
        pass
    
    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def sacar(self):
        pass

@dataclass
class Pessoa:
    nome: str
    cpf: str

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}'

    def __del__(self):
        print(f'Objeto {self.nome} destruído.')

@dataclass
class Conta(IConta):
    agencia: str
    numero: str
    saldo: float
    titular: Pessoa

    def __str__(self):
        return f'Conta {self.numero} criada com sucesso!'

    def __float__(self):
        return self.saldo
    
    def __del__(self):
        print('Conta excluída com sucesso!')

    def consultar(self):
        print('Titular da conta:')
        print(self.titular)
        print(f'Agência: {self.agencia}')
        print(f'Número da conta: {self.numero}')
        print(f'Saldo: {self.saldo}')

    def depositar(self,valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self,valor):
        self.saldo -= valor
        return self.saldo

@dataclass
class ContaCorrente(Conta):
    taxa: float

    def sacar(self, valor,taxa):
        valor += taxa
        return super().sacar(valor)

@dataclass
class ContaPoupanca(Conta):
    juros: float

    def depositar(self, valor,juros):
        valor += (juros/100)
        return super().depositar(valor)