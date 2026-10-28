from mod import eq_1grau, li

def main():
    li
    a = float(input('Digite o valor de "a": ').replace(',','.'))
    b = float(input('Digite o valor de "b": ').replace(',','.'))
    x = eq_1grau(a,b)
    print(f'O valor de x é: {x}')

if __name__ == '__main__':
    main()