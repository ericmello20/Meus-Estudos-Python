# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("digite o primeiro numero:\n"))
num2 = int(input("digite o segundo numero:\n"))
soma = 0
for n in range(num1+1, num2):
    print(n)
    soma += n
for n in range(num2+1, num1):
    print(n)
    soma += n
print(soma)
