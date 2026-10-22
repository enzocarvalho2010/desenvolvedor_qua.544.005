import os

# cadastro de usuários novos
users = []

os.system("cls")

while True:
    # menu
    print('1. Cadastrar novo usuário.')
    print('2. Exibir lista de usuários.')
    print('3. Encerrar o programa.')
    op = input('Digite a opção desejada:')

    os.system('cls')

    match op:
        case '1':
            # cria novo dicionário
            user = {}

            # insere os dados no dicionário
            user['nome'] = input('Insira o nome do usuário: ').strip().title()
            user['idade'] = int(input('Insira a idade do usuário: '))
            user['email'] = input('Insira o email do usuário: ').strip().lower()
            user['cpf'] = str(input('Insira o cpf do usuário: ')).strip()

            # insere dados do usuário na lista
            users.append(user)
            print(f'{user.get('nome')} cadastrado com sucesso :D')
            
        case '2':
            os.system('cls')
            for user in users:
                for chave, valor in user.items():
                    print(f'{chave.capitalize()}: {valor}')
                print(f'{40*'-'}')

        case '3':
            break
        case _:
            print('Opção invlida :(')
            continue