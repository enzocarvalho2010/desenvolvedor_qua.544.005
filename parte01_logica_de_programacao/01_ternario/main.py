# declaração de variáveis
nome = str(input('Digite o seu nome: ')).strip().title()
idade = int(input('Digite a sua idade: '))

#operador ternário
print(f'{nome} {'é maior de idade' if idade >= 18 else 'é menor de idade'}')