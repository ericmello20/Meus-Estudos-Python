#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
#Ano bissexto deve ser múltiplo de 4 mas não pode ser múltiplo de 100, a menos que seja multiplo de 400.
ano=int(input("Digite um ano:\n"))
if (ano%4==0 and ano%100!=0) or ano%400==0:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")