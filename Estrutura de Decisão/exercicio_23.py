#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
numero=float(input("digite um numero:\n"))
if numero%1==0:
    print("inteiro")
else:
    print("decimal")