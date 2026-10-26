import os

user = {'nome':"Bruce Wayne"
        ,'idade': 45
        ,'email':"batima@gmail.com"
        ,'telefone': "(67) 96767-4242"
        ,'endereço': 'Bat-Caverna'}

# exibe a lista original
for chave, valor in user.items():
    print(f'{chave}: {valor}')

# informa a chave a ser deletada
chave_escolhida = input('Informe a chave a ser deletada: ').strip().lower()

os.system('cls')

# deleta a chave
del user[chave_escolhida]

# exibe o dicionário atualizado
for chave, valor in user.items():
    print(f'{chave}: {valor}')