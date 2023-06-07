# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("digite um numero inteiro!\n"))
contador = 1
divisivel = 0

while contador <= numero:
    if numero % contador == 0:
        divisivel += 1
    contador += 1

if divisivel == 2:
    print("É primo!")
else:
    print("Não é primo!")
