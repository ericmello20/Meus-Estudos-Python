# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = C * 1.8 + 32

temperatura = float(input("Digite a temperatura em graus Celsius:\n"))
conversao = temperatura * 1.8 + 32
print("A temperatura convertida para graus Fahrenheit é igual a %.4f" % (conversao))
