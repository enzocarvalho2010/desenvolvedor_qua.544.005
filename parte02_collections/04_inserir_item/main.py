# Programa para inserir uma lista de tarefas a fazer
import os

 # lista vazia
tarefas = []

os.system('cls')

while True:

    print('1. Inserir nova tarefa à lista.')
    print('2. Encerrar e exibir lista.')

    op = input('Opção desejada: ')

    match op:
        case '1':
            os.system('cls')
            
            nova = (input('Insira uma nova tarefa: ').strip().title())
            tarefas.append(nova)
            continue
        case '2':
            os.system('cls')

            #exibe a lista:
            for n, tarefa in enumerate(tarefas, start=1):
                print(f'{n}ª tarefa: {tarefa}')
            break
        case _:
            print('Opção inválida.')