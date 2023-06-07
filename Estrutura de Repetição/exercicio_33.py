'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, 
e informe ao final a menor e a maior temperaturas informadas, 
bem como a média das temperaturas.
'''


lista_temperaturas = []
aux = True
soma = 0
contador = 0

while aux == True:
    temperatura = int(input("digite uma temperatura:\n"))

    if temperatura != 0:
        lista_temperaturas.append(temperatura)
        soma += temperatura
        contador += 1
        aux = True

    else:
        aux = False

maior_temperatura = max(lista_temperaturas)
menor_temperatura = min(lista_temperaturas)
media_temperatura = soma/contador

print("A maior temperatura informada foi: %d" % (maior_temperatura))
print("A menor temperatura informada foi: %d" % (menor_temperatura))
print("A média das temperaturas informadas é: %d" % (media_temperatura))
