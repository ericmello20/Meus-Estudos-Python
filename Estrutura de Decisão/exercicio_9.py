# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input("Digite o primeiro numero:\n"))
num2 = float(input("Digite o segundo numero:\n"))
num3 = float(input("digite o terceiro numero:\n"))
if num1 > num2 and num2 > num3 and num1 > num3:
    print(f"{num1} {num2} {num3}")
elif num1 > num2 and num3 > num2 and num1 > num3:
    print(f"{num1} {num3} {num2}")
elif num2 > num1 and num1 > num3 and num2 > num3:
    print(f"{num2} {num1} {num3}")
elif num2 > num1 and num3 > num1 and num2 > num3:
    print(f"{num2} {num3} {num1}")
elif num3 > num1 and num1 > num2 and num3 > num2:
    print(f"{num3} {num1} {num2}")
elif num3 > num1 and num2 > num1 and num3 > num2:
    print(f"{num3} {num2} {num1}")
