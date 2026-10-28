from mod import eq_2grau, li

def main():
    a = float(input('Digite o valor de "a": ').replace(',',','))
    b = float(input('Digite o valor de "b": ').replace(',',','))
    c = float(input('Digite o valor de "c": ').replace(',',','))
    li()

    if a != 0:
        r = eq_2grau(a,b,c)
        print('Resultado da equação do 2º grau: ')
        for x in r:
            print(f'x = {x}')
    else:
        print('Os valores não correspondem a uma equação do 2º grau.')

if __name__ == '__main__':
    main()