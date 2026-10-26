# tratamento de exceção
''' usa-se para descobrir um erro no código
tem q usar o '#todo' em caixa alta pra lembrar de fazer o código dps
tem q usar o '#fixme' em caixa alta pra lembrar de consertar o código dps
tem q usar o '#review' em caixa alta pra lembrar de revisar o código dps
'''
try:
    n = input('Informe seu nome: ').strip().title()
    i = int(input('Informe a sua idade: '))

    print(f'Nome: {n}')
    print(f'Idade: {i} anos')
except Exception as e:
    print(f'Não foi possível executar a ação :( {e}')
finally:
    print('Programa finalizado com sucesso :D')