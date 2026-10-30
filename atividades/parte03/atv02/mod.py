import os
li = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def fi():
    a = 0
    b = 1
    x = int(input('Insira o número de termos: '))
    if x == 0:
        print(0)
    else:
        for i in range(x):
            c = a+b
            a=b 
            b=c
            print(f'{a}')
    