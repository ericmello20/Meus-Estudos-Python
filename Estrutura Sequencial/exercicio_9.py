# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temperatura = float(input("Digite a temperatura em graus Fahrenheit:\n"))
conversao = 5*((temperatura-32)/9)
print("A temperatura convertida para graus Celsius é igual a %.4f" % (conversao))
