import os
import json

users = []
os.system('cls')

while True:
    try:
        print('1. Cadastrar usuário.')
        print('2. Gravar arquivo JSON.')
        print('3. Exibir usuários.')
        print('4. Alterar credencial de um usuário.')
        print('5. Deletar usuário.')
        print('6. Encerrar programa.')
        op = input('Digite a opção desejada: ').strip()

        os.system('cls')

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
                for user in users:
                    for chave, valor in user.items():
                        print(f'{chave.capitalize()}: {valor}')
                    print(f'{'-'*40}')
                    cont = input('Deseja salvar os dados? (s/n): ')
                    if cont == 's':
                        os.system('cls')
                        arq = input('Digite o nome do arquivo a ser criado: ').strip()
                        with open(f'atv01/{arq}.json','w',encoding='utf-8') as f:
                            users = json.dump(users,f)
                        print('Arquivo gravado com sucesso :D')
                        continue
                    else:
                        os.system("cls")
                        continue
            case '3':
                try:
                    abrir = input('Insira o nome do arquivo a ser aberto: ').strip()
                    with open(f'atv01/{abrir}.json','r',encoding = 'utf-8') as f:
                        users = json.load(f)
                    for user in users:
                        for chave,valor in user.items():
                            print(f'{chave.capitalize()}: {valor}')
                    print(f'{'-'*40}')
                except Exception as e:
                    print(f'Algo deu errado ---> {e}')
                continue

            case '4':
                abrir = input('Insira o nome do arquivo a ser aberto: ').strip()
                with open(f'atv01/{abrir}.json','r',encoding = 'utf-8') as f:
                        users = json.load(f)
                for user in users:
                        for chave,valor in user.items():
                            print(f'{chave.capitalize()}: {valor}')
                print(f'{'-'*40}')
                user = {}

                user['nome'] = input('Novo nome: ').strip().title()
                user['email'] = input('Novo email: ').strip().lower()
                user['telefone'] = input('Novo telefone: ')
                user['cpf'] = input('Novo CPF: ').strip()
                with open(f'atv01/{abrir}.json','w',encoding = 'utf-8') as f:
                    users = json.dump(user,f)
                print('Arquivo alterado com sucesso :D')

            case '5':
                try:
                    abrir = input('Insira o nome do arquivo a ser aberto: ').strip()
                    os.remove(f'atv01/{abrir}.json')

                except Exception as e:
                    print(f'Algo deu errado ---> {e}')

            case '6':
                print('Programa encerrado')
                break

            case _:
                print('Opção inválida :(')
                continue
    except Exception as e:
        print(f'Algo deu errado ---> {e}')