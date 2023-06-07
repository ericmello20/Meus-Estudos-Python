# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Digite quanto você ganha por hora:\n"))
horas = float(input("Digite quantas horas você trabalhou no mês:\n"))
salario = salario_hora*horas
print("O seu salário no mês é %.2f" % (salario))
