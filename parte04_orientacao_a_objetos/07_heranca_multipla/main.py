import os
from model import CarroVoador

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    carrov = CarroVoador(cambio=True
        ,estepe=False
        ,porta_malas=False
        ,volante=True
        ,retrovisor=True
        ,buzina=True
        ,escapamento=True
        ,asa=True
        ,turbina=True
        ,aerofolio=True
        ,cauda=True
        ,manche=True
        ,caixa_preta=True)
    li()
    print(f'Câmbio: {carrov.cambio}')
    print(f'Estepe: {carrov.estepe}')
    print(f'Porta Malas: {carrov.porta_malas}')
    print(f'Volante: {carrov.volante}')
    print(f'Retrovisor: {carrov.retrovisor}')
    print(f'Buzina: {carrov.buzina}')
    print(f'Escapamento: {carrov.escapamento}')
    print(f'Asa: {carrov.asa}')
    print(f'Turbina: {carrov.turbina}')
    print(f'Aerofólio: {carrov.aerofolio}')
    print(f'Cauda: {carrov.cauda}')
    print(f'Manche: {carrov.manche}')
    print(f'Caixa Preta: {carrov.caixa_preta}')

if __name__ == '__main__':
    main()