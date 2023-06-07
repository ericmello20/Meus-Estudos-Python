# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
# meses com 31 dias: 1 3 5 7 8 10 12
# fevereiro mes 2 apenas 28 dias, exceto no ano bissexto q vai até 29
# meses com 30 dias: 4 6 9 11
dia = int(input("Digite o dia no formato \'dd\':\n"))
mes = int(input("Digite o mes no formato \'mm\':\n"))
ano = int(input("Digite o ano no formato \'aaaa\':\n"))

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia <= 31:
    print("data válida!")

elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia <= 30:
    print("data válida!")

elif mes == 2:
    if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0) and dia <= 29:
        print("data válida!")
    else:
        print("data inválida")

elif dia <= 28:
    print("data válida!")

else:
    print("data inválida!")
