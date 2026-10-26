user = {'nome':"Enzo Carvalho"
        ,'idade': 16
        ,'altura': 1.69
        ,'email':"zitom@gmail.com"
        ,'cpf':"060.070.067-42"
        ,'telefone': "(67) 96767-4242"}

# exibe um valor especíco.
print(f'Nome: {user['nome']}')
print(f'E-mail: {user.get('email')}')

# percorre o dicionário
for chave, valor in user.items():
    print(f'{chave.capitalize()}: {valor}.')