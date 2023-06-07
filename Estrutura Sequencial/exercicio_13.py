# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input("digite o sexo da pessoa(\"h\" para homem e \"m\" para mulher):\n")
altura = float(input("digite a altura da pessoa:\n"))
if sexo == "h":
    peso_ideal = (72.7*altura)-58
else:
    peso_ideal = (62.1*altura)-44.7
print("O peso ideal para esta pessoa é %.2f" % (peso_ideal))
