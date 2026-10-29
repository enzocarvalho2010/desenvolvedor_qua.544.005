import os

li = lambda: os.system('cls' if os.name == 'nt' else 'clear')
a_tri = lambda b,h: (b*h)/2

def main():
    li()
    b = float(input('Digite o valor da base: ').replace(',','.').replace('-',''))
    h = float(input('Digite o valor da altura: ').replace(',','.').replace('-',''))
    li()
    print(f"Àrea do triângulo: {a_tri(b,h)}")

if __name__ == '__main__':
    main()