import os

# declaração de funções
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def boas_vindas(nome):
    return f'Seja bem vindo, {nome}!'

# algoritmo principal
limpar()
nome = input('Digite seu nome: ').strip().title()
print(boas_vindas(nome))