import mod

def main():
    while True:
        try:
            print('1. Mercúrio')
            print('2. Vênus')
            print('3. Terra')
            print('4. Lua')
            print('5. Marte')
            print('6. Júpiter')
            print('7. Saturno')
            print('8. Urano')
            print('9. Netuno')
            op = input('Digite o número correspondente ao planeta: ').strip()
            m = float(input('Digite a massa em quilogramas: ').strip().replace(',','.'))
            mod.li()

            match op:
                case '1':
                    print(f'A massa {m} em Mercúrio equivale a {mod.mer(m):.2f}N.')
                case '2':
                    print(f'A massa {m} em Vênus equivale a {mod.ven(m):.2f}N.')
                case '3':
                    print(f'A massa {m} na Terra equivale a {mod.ter(m):.2f}N.')
                case '4':
                    print(f'A massa {m} em Lua equivale a {mod.lua(m):.2f}N.')
                case '5':
                    print(f'A massa {m} em Marte equivale a {mod.mar(m):.2f}N.')
                case '6':
                    print(f'A massa {m} em Júpiter equivale a {mod.jup(m):.2f}N.')
                case '7':
                    print(f'A massa {m} em Saturno equivale a {mod.sat(m):.2f}N.')
                case '8':
                    print(f'A massa {m} em Urano equivale a {mod.ura(m):.2f}N.')
                case '9':
                    print(f'A massa {m} em Netuno equivale a {mod.net(m):.2f}N.')
                case _:
                    print('Opção inválida :(')
                    continue
            print(f'{'-'*40}')
            break
        except Exception as e:
            print(f'Algo deu errado --> {e}')
if __name__ == '__main__':
    main()