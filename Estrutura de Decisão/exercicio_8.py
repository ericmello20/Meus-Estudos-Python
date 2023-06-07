#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
preço1=float(input("digite o valor do produto 1\n"))
preço2=float(input("digite o valor do produto 2\n"))
preço3=float(input("digite o valor do produto 3\n"))
if preço1<preço2 and preço1<preço3:
    print("O produto 1 é o mais barato!")
elif preço2<preço1 and preço2<preço3:
    print("O produto 2 é o mais barato!")
elif preço3<preço1 and preço3<preço2:
    print("O produto 3 é o mais barato!")