cidades = ['Taguatinga'
           ,'Plano Piloto'
           ,'Ceilândia'
           ,'Taguatinga'
           ,'Guará'
           ,'Planaltina'
           ,'Ceilândia'
           ,'Brazlândia'
           ,'Plano Piloto']

item = (input('Digite o nome da cidade: ').strip().title())

#verifica quantas vezes o item foi encontrado
print(f'{item} foi encontrado {cidades.count(item)} vezes na lista.')