'''
Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
'''

lista_primos = []
numero = int(input("Digite um numero!\n"))

for n in range(1, numero+1):
    contador = 0

    for i in range(1, n+1):

        if n % i == 0:

            contador += 1

    if contador == 2:
        lista_primos.append(n)

print(lista_primos)
