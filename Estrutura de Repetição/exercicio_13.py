'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

# CONSEGUI RESOLVER PARA TODAS AS SITUAÇÕES, TANTO COM EXPOENTE NEGATIVO, QUANTO POSITIVO OU 0

base = float(input("digite o valor da base:\n"))
expoente = int(input("digite o valor do expoente:\n"))

if expoente == 0:
    potencia = 1

elif 0 < expoente:
    contador = 1
    potencia = base
    while contador < expoente:
        potencia *= base
        contador += 1

elif expoente < 0:
    contador = -1
    potencia = 1/base
    while contador > expoente:
        potencia *= 1/base
        contador -= 1

print(potencia)
