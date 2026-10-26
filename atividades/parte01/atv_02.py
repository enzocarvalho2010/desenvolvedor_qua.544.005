# atividade 02
import os
os.system('cls')

nome = (input('Digite o seu nome: ').strip().title())
age = int(input('Digite a sua idade: '))

os.system('cls')

while True:
    print(f'{'-'*20}> Filmes Disponíveis <{'-'*20}')
    print('Sala 1 - Super Mario Galaxy [L]')
    print('Sala 2 - Michael [+12]')
    print('Sala 3 - Avangers: Doomsday [+14]')
    print('Sala 4 - A Odisseia [+16]')
    print('Sala 5 - Obsessão [+18]')

    try:
        filme = int(input('Digite a sala correspondente ao filme escolhido: ').strip())
        match filme:
            case 1:
                if age >= 0:
                    print('Ingresso comprado para Super Mario Galaxy; sala 01. Bom filme!')
                    print('Obrigado! Volte sempre :D')
                    break
                else:
                    print('Ops... Você não possue a idade mínima para consumir o conteúdo :(')
            case 2:
                if age >= 12:
                    print('Ingresso comprado para Michael; sala 02. Bom filme!')
                    print('Obrigado! Volte sempre :D')
                    break
                else:
                    print('Ops... Você não possue a idade mínima para consumir o conteúdo :(')
            case 3:
                if age >= 14:
                    print('Ingresso comprado para Avengers: Doomsday; sala 03. Bom filme!')
                    print('Obrigado! Volte sempre :D')
                    break
                else:
                    print('Ops... Você não possue a idade mínima para consumir o conteúdo :(')
            case 4:
                if age >= 16:
                    print('Ingresso comprado para A Odisseia; sala 04. Bom filme!')
                    print('Obrigado! Volte sempre :D')
                    break
                else:
                    print('Ops... Você não possue a idade mínima para consumir o conteúdo :(')
            case 5:
                if age >= 18:
                    print('Ingresso comprado para Obsessão; sala 05. Bom filme!')
                    print('Obrigado! Volte sempre :D')
                    break
                else:
                    print('Ops... Você não possue a idade mínima para consumir o conteúdo :(')
            case _:
                print('O filme não está no catálogo :(')
        cont = (input('Deseja escolher o filme novamente? "sim" para prosseguir. Qualquer outra tecla para encerrar: ').strip().lower())
        
        if cont == 'sim':
            os.system('cls')
            continue
        else:
            break
    except Exception as e:
        print(f'Não foi possível escolher o filme. {e}')