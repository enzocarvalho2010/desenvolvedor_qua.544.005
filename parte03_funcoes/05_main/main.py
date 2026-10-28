import math
import os

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def raiz(n):
    return math.sqrt(n)

# algorítmo principal
def main():
    li()
    n = int(input('Digite um número: ').strip())
    print(f'Raíz de {n}: {raiz(n):.0f}')

# algorítmo principal protegido
if __name__ == '__main__':
    main()