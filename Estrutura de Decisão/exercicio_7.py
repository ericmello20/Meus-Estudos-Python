# Faça um Programa que leia três números e mostre o maior e o menor deles.
numero1 = float(input("Digite o primeiro numero:\n"))
numero2 = float(input("Digite o segundo numero:\n"))
numero3 = float(input("digite o terceiro numero:\n"))
#encontrando o maior:
maior = numero1
if maior < numero2:
    maior = numero2

if maior < numero3:
    maior = numero3

print(maior)
#encontrando o menor:
menor = numero1
if menor > numero2:
    menor = numero2

if menor > numero3:
    menor = numero3

print(menor)
