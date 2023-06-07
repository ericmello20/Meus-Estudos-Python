# Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

quantidade = int(input(
    "Digite a quantidade de alunos que você quer retirar a média de idades:\n"))
soma = 0
for n in range(1, quantidade+1):
    numero = int(input("Digite a idade do aluno:\n"))
    soma += numero
media = soma/quantidade

if 0 < media <= 25:
    print("A média das idades é: %.2f\nA turma é jovem" % (media))
elif 25 < media <= 60:
    print("A média das idades é: %.2f\nA turma é adulta" % (media))
elif media > 60:
    print("A média das idades é: %.2f\nA turma é idosa" % (media))
else:
    print("Não existe média negativa de idades!")
