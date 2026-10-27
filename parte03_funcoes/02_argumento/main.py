# função
def boas_vindas(nome):
    print(f'{nome}, seja bem vindo')

# algoritmo principal
nome = input('Digite seu nome: ').strip().title()
boas_vindas(nome)