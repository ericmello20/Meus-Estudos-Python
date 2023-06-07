# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

inteiro_a = int(input("digite um valor inteiro: "))
inteiro_b = int(input("digite um valor inteiro: "))
real = float(input("digite um valor real: "))
produto = (2*inteiro_a)*(inteiro_b/2)
soma = 3*inteiro_a+real
elevado = real**3
print("o produto do dobro do primeiro com metade do segundo é: %.2f" % (produto))
print("a soma do triplo do primeiro com o terceiro é: %.2f" % (soma))
print("o terceiro elevado ao cubo é: %.2f" % (elevado))
