'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input("Digite um nome com mais de 3 caracteres:\n")
while len(nome) <= 3:
    print("nome inválido!")
    nome = input("Digite um nome com mais de 3 caracteres:\n")
print("nome válido!")

idade = int(input("digite a idade (entre 0 e 150):\n"))
while 0 > idade or idade > 150:
    print("idade inválida!")
    idade = int(input("digite a idade:\n"))
print("idade válida!")

salario = float(input("digite o salário (maior que 0):\n"))
while salario < 0:
    print("salário inválido!")
    salario = float(input("digite o salário (maior que 0):\n"))
print("salário válido!")

sexo = input("Digite o sexo (\"f\" ou \"m\"):\n")
while sexo not in "fmFM":
    print("sexo inválido!")
    sexo = input("Digite o sexo (\"f\" ou \"m\"):\n")
print("sexo válido!")

estado_civil = input("Digite o estado civil (\"s\", \"c\", \"v\", \"d\"):\n")
while estado_civil not in "scvdSCVD":
    print("estado civil inválido!")
    estado_civil = input(
        "Digite o estado civil (\"s\", \"c\", \"v\", \"d\"):\n")
print("estado civíl válido!")
