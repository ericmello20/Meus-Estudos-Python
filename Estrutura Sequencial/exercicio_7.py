# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# A área do quadrado é lado**2, portanto, necessário pedir o valor do lado do quadrado para calcular.

lado = float(input("Digite o valor do lado do quadrado:\n"))
area = lado**2
print("A área do quadrado é: %.4f" % (area))
