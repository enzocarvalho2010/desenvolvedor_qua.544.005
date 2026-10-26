dias = ('Domingo'
        ,'Segunda-Feira'
        ,'Terça-Feira'
        ,'Quarta-Feira'
        ,'Quinta-Feira'
        ,'Sexta-Feira'
        ,'Sábado')

for dia in dias:
    print(dia)


#NOTE: se tentar mudar a lista, o programa dá erro.
try:
    dias.sort()
    for dia in dias:
        print(dia)

except Exception as e:
    print(f'Deu ruim :( {e}')