#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
#Depois modifique o programa para que ele mostre os números um ao lado do outro.

#APRIMOREI PARA QUE O USUÁRIO DIGA QUAL O NÚMERO ELE QUER QUE SEJA CONTADO

numero=int(input("Digite um numero: "))
for i in range (1,numero+1):
    print (i)
print(list(range(1,numero+1)))

#O PROGRAMA ORIGINAL (COMO PEDE O ENUNCIADO) SERIA:

#for i in range (1,21):
#    print (i)
#print(list(range(1,21)))