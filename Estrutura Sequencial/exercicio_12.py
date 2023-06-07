# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("digite a altura da pessoa: \n"))
peso_ideal = (72.7*altura)-58
print("O peso ideal para esta pessoa é %.2f" % (peso_ideal))
