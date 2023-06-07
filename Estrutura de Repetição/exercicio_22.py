# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

numero = int(input("digite um numero inteiro!\n"))
contador = 1
divisivel = 0
lista_divisiveis = []

while contador <= numero:
    if numero % contador == 0:
        lista_divisiveis.append(contador)
        divisivel += 1
    contador += 1

if divisivel != 2:
    print("Não é primo!")
    print("É divisivel por:\n", lista_divisiveis)
else:
    print("É primo!")
