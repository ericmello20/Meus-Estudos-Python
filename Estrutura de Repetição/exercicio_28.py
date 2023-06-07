'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

quantidade_cds = int(input("Digite a quantidade de CD's:\n"))

soma = 0

for n in range(1, quantidade_cds+1):
    valor_cds = float(input("Digite o preço do CD:\n"))
    soma += valor_cds

media = soma/quantidade_cds

print("O valor total investido foi: R$%.2f" % (soma))
print("A média gasta em cada CD foi: R$%.2f" % (media))
