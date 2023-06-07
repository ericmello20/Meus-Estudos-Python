'''Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.'''

turmas = int(input("Digite a quantidade de turmas:\n"))
soma = 0
for n in range(1, turmas+1):
    alunos = int(input("Digite a quantidade de alunos na turma:\n"))
    if alunos > 40 or alunos < 0:
        print("A turma não pode ter + de 40 alunos!\nDigite novamente!")
        alunos = int(input("Digite a quantidade de alunos na turma:\n"))
    soma += alunos
media = soma/turmas
print("A média de alunos por turma é: %.2f" % (media))
