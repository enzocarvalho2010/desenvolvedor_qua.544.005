# JavaScript Object Notation (JSON)

import json
import os

users = []
os.system('cls')

while True:
    try:
        print('1. Cadastrar novo usuário.')
        print('2. Gravar novo arquivo JSON.')
        print('3. Abrir arquivo.')
        print('4. Encerrar programa.')
        op = input('Digite a opção desejada: ').strip()
        os.system('cls')
        match op:
            case '1':
                user = {}

                user['nome'] = input('Insira o nome: ').strip().title()
                user['idade'] = int(input('Insira a idade: ').strip())
                user['email'] = input('Insira o email: ').strip().title()
                user['cpf'] = input('Insira o CPF: ').strip()
                user['telefone'] = input('Insira o telefone: ').strip()

                users.append(user)
                os.system('cls')

                print(f'Usuário {user.get('nome')} cadastrado com sucesso :D')
                continue
            case '2':
                for user in users:
                    for chave, valor in user.items():
                        print(f'{chave.capitalize()}: {valor}')
                    print(f'{'-'*40}')

                    prosseguir = input('Deseja gravar os dados? (s/n): ').strip().lower()

                    if prosseguir == 's':
                        os.system('cls')
                        arq = input('Digite o nome do arquivo: ').strip()
                        with open(f'16_JSON/{arq}.json','w',encoding='utf-8') as f:
                            json.dump(users,f)
                        print('Arquivo JSON gravado com sucesso :D')
                    else:
                        os.system('cls')
                        continue

            case '3':
                os.system('cls')
                try:
                    abrir = input('Insira o nome do arquivo a ser aberto: ').strip()
                    with open(f'16_JSON/{abrir}.json','r',encoding='utf-8') as f:
                        users = json.load(f)
                    for user in users:
                        for chave, valor in user.items():
                            print(f'{chave.capitalize()}: {valor}')
                        print(f'{'-'*40}')
                    continue
                except Exception as e:
                    print(f'Algo deu errado ---> {e}')
                continue
            case '4':
                print('Programa encerrado.')
                break
# linha SIX SEVEEN!!!
            case _:
                print('Opção inválida :(')
                continue

    except Exception as e:
        print(f'Algo deu errado ---> {e}')