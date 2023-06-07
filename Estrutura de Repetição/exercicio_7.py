#Faça um programa que leia 5 números e informe o maior número.

#APRIMOREI PARA QUE O USUÁRIO DIGA QUANTOS NÚMEROS ELE QUER QUE SEJAM COMPARADOS!

#APRENDI A USAR A FUNÇÃO MAX() QUE COMPARA OS VALORES DA LISTA E SELECIONA O MAIOR DELES.

lista_num=[]
numeros=int(input("digite a quantidade de números:\n"))
for maior in range (1,numeros+1):
    lista_num.append(float(input("digite o numero:\n")))
print("O maior número digitado foi: ", max(lista_num))

#O PROGRAMA ORIGINAL (COMO PEDE O ENUNCIADO) SERIA:

#lista_num=[]
#for maior in range (5):
#    lista_num.append(float(input("digite o numero:\n")))
#print("O maior número digitado foi: ", max(lista_num))
