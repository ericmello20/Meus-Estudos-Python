# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota entre 0 e 10:\n"))
while 0 > nota or nota > 10:
    nota = float(input("Digite uma nota entre 0 e 10:\n"))
print("valor válido!")
