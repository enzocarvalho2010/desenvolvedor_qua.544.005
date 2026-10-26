# atividade 01
import os
# variáveis:
os.system('cls')
nome = (input('Digite o seu nome: ').strip().title())
kg = float(input('Digite o seu peso em quilogramas: ').replace(',','.'))
alt = float(input('Digite sua altura em metros: ').replace(',','.'))

imc = (kg) / (alt*alt)

os.system('cls')

print(f'O IMC de {nome} é {imc:.2f}')
if imc < 18.5:
    print(f'{nome} está abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print(f'{nome} possui peso adequado.')
elif imc >= 25 and imc <= 29.9:
    print(f'{nome} possui sobrepeso.')
elif imc >= 30 and imc <= 34.9:
    print(f'{nome} possui obesidade grau I.')
elif imc >= 35 and imc <= 39.9:
    print(f'{nome} possui obesidade grau II.')
elif imc >= 40:
    print(f'{nome} possui obesidade grau III.')
else:
    print('IMC inválido')