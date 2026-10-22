# lista de dicionários
users = [{
        'nome':"Ney Gaúcho"
        ,'idade': 67
        ,'email':"arroganthi@gmail.com"
        },
        {
        'nome':"Peter Parker"
        ,'idade': 17
        ,'email':"miranha@gmail.com"
        },
        {
        'nome':"Michael Jackson"
        ,'idade': 42
        ,'email':"whosbad@gmail.com"
        }]

for user in users:
    for chave, valor in user.items():
        print(f'{chave.capitalize()}: {valor}')
    print(f'{'-'*40}')