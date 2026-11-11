import os
from translate import Translator 

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def traduzir(texto):
    tradutor = Translator(to_lang='pt')
    return tradutor.translate(texto)

def main():
    li()
    texto = input('Insita o texo a ser traduzido: ')
    print(f'\nTexto traduzido:\n{traduzir(texto)}')

if __name__ == '__main__':
    main()