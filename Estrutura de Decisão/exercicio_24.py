'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''
numero1 = float(input("digite o primeiro número:\n"))
numero2 = float(input("digite o segundo número:\n"))
operação = input("Qual operação você deseja realizar? \n\"+\"\n\"-\"\n\"*\"\n\"/\"\n")

if operação == "+":
    total = numero1+numero2

elif operação == "-":
    total = numero1-numero2

elif operação == "*":
    total = numero1*numero2

elif operação == "/":
    total = numero1/numero2

print("O resultado da operação é %.2f" % (total))

if total % 2 == 0:
    print("par")
else:
    print("impar")
if total >= 0:
    print("positivo")
else:
    print("negativo")
if total % 1 == 0:
    print("inteiro")
else:
    print("decimal")
