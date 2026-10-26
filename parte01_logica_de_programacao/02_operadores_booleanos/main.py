# declaração de variáveis
n = input('Digite o seu nome: ').strip().title()
i = int(input('Digite a sua idade: '))
h = float(input('Digite a sua altura em metros: ').replace(',','.'))

# verificação dos pré-requisitos
if i >=12 and h >= 1.35:
    print(f'{n} está autorizado a entrar :)')
else:
    print(f'{n} não está autorizado a entrar :(')