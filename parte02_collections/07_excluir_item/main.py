# lista
frutas = ['Maçã'
          ,'Maracujá'
          ,'Uva'
          ,'Pêra'
          ,'Manga'
          ,'Kiwi'
          ,'Melancia'
          ,'Goiaba']

while True:
    for n, fruta in enumerate(frutas):
        print(f'Índice {n}: {fruta}')

    # menu
    print('1. Alterar fruta.')
    print('2. Encerrar programa.')
    op = input('Digite a opção desejada: ').strip()

    # verifica opção
    match op:
        case '1':
            indice = int(input('Informe o índice a ser excluído: '))
            del(frutas[indice])
            print('Fruta excluída com sucesso!')
            continue
        
        case '2':
            print('Programa encerrado com sucesso.')
            break
        
        case _:
            print('Opção inválida.')
            continue