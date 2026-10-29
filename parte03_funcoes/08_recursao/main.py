import os

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def fatorial(n):
    return 1 if n == 1 else n*fatorial(n-1)

def main():
    li()
    try:
        n = int(input('Informe o número natural: ').replace('-',''))
        li()
        print(f'{n}! = {fatorial(n)}')
    except Exception as e:
        print(f'Algo deu errado --> {e}')

if __name__ == '__main__':
    main()