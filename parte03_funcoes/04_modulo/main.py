import mod

mod.li()
while True:
        print('1. Calcular área do quadrilátero.')
        print('2. Calcular área do círculo.')
        print('3. Calcular comprimento do círculo.')
        print('4. Encerrar programa.')
        op = input('Digite a opção desejada: ').strip()
        mod.li()

        match op:
            case '1':
                mod.li()
                b = float(input('Valor da base: ').replace(',','.'))
                h = float(input('Valor da altura: ').replace(',','.'))
                a = mod.a_quad(b,h)
                print(f'Área do quadrilátero: {a:.2f}')
                print(f'{'-'*40}')
                continue
            case '2':
                mod.li()
                r = float(input('Valor do raio: ').replace(',','.'))
                a = mod.a_circ(r)
                print(f'Área do círculo: {a:.2f}')
                print(f'{'-'*40}')
                continue
            case '3':
                mod.li()
                r = float(input('Valor do raio: ').replace(',','.'))
                c = mod.cum_circ(r)
                print(f'Comprimento do círculo: {c:.2f}')
                print(f'{'-'*40}')
                continue
            case '4':
                mod.li()
                print('Programa encerrado.')
                print(f'{'-'*40}')
                break
            case _:
                print('Opção inválida :(')
                continue