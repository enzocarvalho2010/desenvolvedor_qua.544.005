user = {'nome':'Fulano de Tal'
        ,'idades': 18 
        ,'email':'fulano@gmail.com'}

# usuário informar o nome da nova chave
nchave = input('Informe uma nova credencial: ').strip().lower()

# usuário informa o valor da nova chave
user[nchave] = input('Insira a nova credencial: ').strip()

# exibe o dicionário
for chave, valor in user.items():
    print(f'{chave.capitalize()}: {valor}.')