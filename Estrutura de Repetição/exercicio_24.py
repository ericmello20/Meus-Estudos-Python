# Faça um programa que calcule e mostre a média aritmética de N notas.

quantidade = int(
    input("Digite a quantidade de numeros que você quer retirar a média:\n"))
soma = 0
for n in range(1, quantidade+1):
    numero = float(input("Digite o numero:\n"))
    soma += numero
media = soma/quantidade
print("A média dos numeros é: %.2f" % (media))
