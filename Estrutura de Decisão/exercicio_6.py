# Faça um Programa que leia três números e mostre o maior deles.
numero1 = float(input("Digite o primeiro numero:\n"))
numero2 = float(input("Digite o segundo numero:\n"))
numero3 = float(input("digite o terceiro numero:\n"))
if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero1 and numero2 > numero3:
    print(numero2)
elif numero3 > numero1 and numero3 > numero2:
    print(numero3)
