import os

os.system('cls' if os.name == "nt" else 'clear')

while True:
    n = (input('Digite o nome do aluno: ').strip().title())
    try:
        n1 = float(input('Digite a primeira nota do aluno: ').replace(',','.'))
        if n1 >= 0 and n1 <= 10:
            if n1 >= 7:
                print(f'{n} está aprovado :)')
            elif n1 >= 5:
                print(f'{n} está de recuperação :/')
            else:
                print(f'{n} está reprovado :(')
        else:
            print('Nota inválida :(')

    except Exception as e:
        print(f'Não foi possível calcular a média. {e}.')
    cont = (input('Deseja inserir outra nota? "sim" para prosseguir. Qualquer outro valor para encerrar: ').strip().lower())

    if cont == "sim":
        os.system('cls' if os.name == "nt" else 'clear')
        continue
    else:
        break