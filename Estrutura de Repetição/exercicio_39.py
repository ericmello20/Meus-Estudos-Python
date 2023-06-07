'''
Faça um programa que leia dez conjuntos de dois valores, 
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

aluno_alto=0
aluno_baixo=500

codigo_aluno_alto=0
codigo_aluno_baixo=0

for i in range(1,11):
    
    altura=float(input("Digite a altura do aluno: "))
    
    if altura>aluno_alto:
        aluno_alto=altura
        codigo_aluno_alto=i
    
    if altura<aluno_baixo:
        aluno_baixo=altura
        codigo_aluno_baixo=i

print("O código do aluno mais alto é: %d; e sua altura é: %.2f"%(codigo_aluno_alto,aluno_alto))
print("O código do aluno mais baixo é: %d; e sua altura é: %.2f"%(codigo_aluno_baixo,aluno_baixo))


