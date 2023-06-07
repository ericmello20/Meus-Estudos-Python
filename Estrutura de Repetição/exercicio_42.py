'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
'''

conjunto_0_25 = 0
conjunto_26_50 = 0
conjunto_51_75 = 0
conjunto_76_100 = 0

while True:
    numero = float(input("Digite um numero POSITIVO: "))
    if numero < 0:
        break
    else:
        if 0 <= numero <= 25:
            conjunto_0_25 += 1
        elif 26 <= numero <= 50:
            conjunto_26_50 += 1
        elif 51 <= numero <= 75:
            conjunto_51_75 += 1
        elif 76 <= numero <= 100:
            conjunto_76_100 += 1
print("No intervalo de 0 até 25 há %d números" % (conjunto_0_25))
print("No intervalo de 26 até 50 há %d números" % (conjunto_26_50))
print("No intervalo de 51 até 75 há %d números" % (conjunto_51_75))
print("No intervalo de 76 até 100 há %d números" % (conjunto_76_100))
