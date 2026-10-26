x = float(input('Digite um número: ').replace(',','.'))
y = float(input('Digite outro número: ').replace(',','.'))

print(f'{'-'*20} Escolha uma operação {'-'*20}')
print('Soma: 1')
print('Subtração: 2')
print('Multiplicação: 3')
print('Divisão: 4')

op = int(input('Operação desejada: ').strip())

match op:
    case 1:
        print(f'Resultado da soma: {x+y}')
    case 2:
        print(f'Resultado da subtração: {x-y}')
    case 3:
        print(f'Resultado da multiplicação: {x*y}')
    case 4:
        print(f'Resultado da divisão: {x/y}')
    case _:
        print('Operação inválida :(')