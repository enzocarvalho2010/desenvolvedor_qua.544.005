import os
from model import Empresa,Departamento

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    departamento = Departamento(nome='')
    emp = Empresa(razao='',fantasia='',cnpj='',departamento=departamento)
    li()

    print('Insira os dados da empresa:')
    emp.razao = input('Digite a razão social: ').strip()
    emp.fantasia = input('Digite o nome: ').strip()
    emp.cnpj = input('Digite o CNPJ: ').strip()
    emp.departamento.nome = input('Digite o departamento: ').strip()
    li()
    print(emp.detalhes())

if __name__ == '__main__':
    main()