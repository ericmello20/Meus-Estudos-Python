# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

# SISTEMA DE PERGUNTAS!!!

lista_numeros = []
soma = 0
pergunta = "s"

while pergunta in "Ss":

    num = float(input("digite um numero entre 0 e 1000: \n"))

    if num <= 0 or num >= 1000:
        print(">>> numero inválido! <<<")
        pergunta = input(
            "Gostaria de adicionar outro numero ao conjunto (ENTRE 0 E 1000)(S ou N)?\n")

    else:
        lista_numeros.append(num)
        pergunta = input(
            "Gostaria de adicionar outro numero ao conjunto?(S ou N)\n")

print("O maior valor digitado foi: %.2f\nO menor valor digitado foi: %.2f" %
      (max(lista_numeros), min(lista_numeros)))
print("A soma dos valores é: %.2f" % (max(lista_numeros)+min(lista_numeros)))
