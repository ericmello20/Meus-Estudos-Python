'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''

numero = int(input("Digite um numero:\n"))
contador = 0

for n in range(1, numero+1):
    if numero % n == 0:
        contador += 1

if contador == 2:
    print("É primo!")

else:
    print("Não é primo!")
