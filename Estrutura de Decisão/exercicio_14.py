'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

nota1=float(input("digite sua nota 1:\n"))
nota2=float(input("digite sua nota 2:\n"))
media=(nota1+nota2)/2
print("A primeira nota foi: %.2f"%(nota1))
print("A segunda nota foi: %.2f"%(nota2))
print("A média das notas foi: %.2f"%(media))
if 0<=media<4:
    print("Conceito E\nREPROVADO")
if 4<=media<6:
    print("Conceito D\nREPROVADO")
if 6<=media<7.5:
    print("Conceito C\nAPROVADO")
if 7.5<=media<9:
    print("Conceito B\nAPROVADO")
if 9<=media<=10:
    print("Conceito A\nAPROVADO")

