import os

nomes = ['Alex'
         ,'Enzimas'
         ,'Scarlet'
         ,'John'
         ,'Jason'
         ,'Michael'
         ,'Connors']

os.system('cls')

while True:
    # menu
    for n, nome in enumerate(nomes):
        print(f'Índice {n}: {nome}')
    print('1. Alterar item da lista')
    print('2. Finalizar')

    op = input('Digite a opção desejada: '). strip()

    match op:
        case '1':
            indice = int(input('Digite o índice a ser alterado: '). strip())
            # informa novo valor
            nomes[indice] = input('Digite o novo nome:').strip().title()
            os.system('cls')
            print('Item da lista alterado com sucesso!')
            continue
        case '2':
            os.system('cls')
            # exibe nova lista
            for n, nome in enumerate(nomes):
                print(f'Índice {n}: {nome}')
            break
        case _:
            print('Opção inválida.')
            