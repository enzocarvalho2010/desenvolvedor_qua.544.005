import os

while True:
    #menu
    print('1. Gravar novo arquivo.')
    print('2. Abrir e ler arquivo.')
    print('3. Encerrar programa.')
    op = input('Digite a opção desejada: ').strip()

    os.system('cls')

    match op:
        case '1':
            # informa o texto a ser gravado
            nwt = input('Digite o texto: ')
            # informa o nome do arquivo
            narq = input('Digite o nome do arquivo: ').strip()

            #grava o novo arquivo
            with open(f'15_gravando_arquivo/{narq}.txt', 'w', encoding='utf-8') as f:
                f.write(nwt)
            continue
        case '2':
            # abre o arquivo
            abrir = input('Informe o nome do .txt que deseja abrir: ').strip()
            with open(f'15_gravando_arquivo/{abrir}.txt','r',encoding='utf-8') as f:
                texto = f.read()
                os.system('cls')
            # exibe o arquivo na tela
            print(f'{texto}')
            continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida :(')
            continue