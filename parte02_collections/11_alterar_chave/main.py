import os

user = {'nome':"Thor Odinson"
        ,'idade': 1507
        ,'email':"naotenho@gmail.com"
        ,'telefone': "(67) 96767-4242"}

os.system('cls')

while True:
    # exibe o dicionário
    for chave, valor in user.items():
        print(f'{chave}: {valor}')
    
    # informa o nome da chave
    chave_escolhida = input('Digite o nome da chave escolhida ou digite "enter"" para encerrar: ').strip().lower()
    if chave_escolhida:
        # informa novo valor
        user[chave_escolhida] = input('Digite o novo valor: ').strip()
        continue
    else:
        print('Programa encerrado com sucesso!')
        break