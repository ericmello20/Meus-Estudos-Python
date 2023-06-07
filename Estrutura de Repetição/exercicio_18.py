# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista_numeros = []
soma = 0
pergunta = "s"
while pergunta in "Ss":
    num = float(input("digite um numero: \n"))
    soma += num
    lista_numeros.append(num)
    pergunta = input(
        "Gostaria de adicionar outro numero ao conjunto?(S ou N)\n")

print("O maior valor digitado foi: %.2f\nO menor valor digitado foi: %.2f\nA soma dos valores digitados é igual a: %.2f" %
      (max(lista_numeros), min(lista_numeros), soma))
