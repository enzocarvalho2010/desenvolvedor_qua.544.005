import os
import json

users = []
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('1. Cadastrar usuário.')
    print('2. Listar Usuários cadastrados.')
    print('3. Alterar credencial de um usuário.')
    print('4. Deletar usuário.')
    print('5. Gravar todos os usuários em JSON.')
    print('6. Abrir arquivo JSON.')
    print('7. Encerrar programa.')
    op = input('Digite a opção desejada: ').strip()

    os.system('cls' if os.name == 'nt' else 'clear')

    match op:
        case '1':
            user = {}

            user['nome'] = input('Insira o nome: ').strip().title()
            user['email'] = input('Insira o email: ').strip().lower()
            user['telefone'] = input('Insira o telefone: ')
            user['cpf'] = input('Insira o CPF: ').strip()
            
            users.append(user)
            print(f'Usuário {user.get('nome')} cadastrado com sucesso!')
            print(f'{'-'*40}')
            continue

        case '2':
            for i, user in enumerate(users):
                print(f'ID: {i}')
                for chave, valor in user.items():
                    print(f'{chave.capitalize()}: {valor}')
                print(f'{'-'*40}')
                continue 
                
        case '3':
            try:
                indice = int(input('Digite o ID do usuário a ser aleterado: '))
                for chave, valor in users[indice]:
                    print(f'{chave.capitalize()}: {valor}')
                chave = input('Qual chave deseja alterar? ').strip().lower()
                users[indice][chave] = input('Informe o valor: ').strip()
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{users[indice][chave]} de {users[indice].get('nome')} alterado com sucesso :D')
                continue
            except Exception as e:
                print(f'Algo deu errado: {e}')
        case '4':
            try:
                indice = int(input('Digite o ID do usuário a ser deletado: '))
                del users[indice]
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Usuário deletado com sucesso :D')
                continue
            except Exception as e:
                print(f'Algo deu errado: {e}')

        case '5':
            arq = input('Digite o nome do arquivo a ser criado: ').strip()
            with open(f'atv01/{arq}.json','w',encoding = 'utf-8') as f:
                json.dump(users,f)
            os.system("cls" if os.name == 'nt' else 'clear')
            print('Dados gravados com sucesso :D')
            continue

        case '6':
            try:
                abrir = input('Insira o nome do arquivo a ser aberto: ').strip()
                with open(f'atv01/{abrir}.json','r',encoding = 'utf-8') as f:
                    users = json.load(f)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(f'Dados importados com sucesso')
                continue
            except Exception as e:
                print(f'Algo deu errado: {e}')

        case '7':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Programa encerrado')
            break

        case _:
            print('Opção inválida :(')
            continue