import os
import pyjokes
from translate import Translator

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def piadas():
    tradutor = Translator(to_lang='pt')
    piada = pyjokes.get_joke()
    return tradutor.translate(piada)

def main():
    li()
    while True:
        print('0. Encerrar programia')
        print('1. Gerar piada aleatória')
        op = input('Escolha uma opção: ')

        match op:
            case '0':
                break
            case '1':
                print(f'Piada: {piadas()}')
                continue
            case '67':
                print('SIX SEVEEN!!')
            case _:
                print("Opção inválida.")
                continue

if __name__ == '__main__':
    main()