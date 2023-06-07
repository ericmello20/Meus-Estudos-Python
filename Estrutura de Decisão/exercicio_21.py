'''Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''
saque = int(input("digite o valor do saque (mínimo R$10 e máximo R$600):\n"))
if saque < 10 or saque > 600:
    print("Saque inválido!")
else:
    notas_cem = saque//100
    saque -= notas_cem*100
    notas_cinquenta = saque//50
    saque -= notas_cinquenta*50
    notas_dez = saque//10
    saque -= notas_dez*10
    notas_cinco = saque//5
    saque -= notas_cinco*5
    notas_um = saque
    if notas_cem > 0:
        print("Notas de 100: %d" % (notas_cem))
    if notas_cinquenta > 0:
        print("Notas de 50: %d" % (notas_cinquenta))
    if notas_dez > 0:
        print("Notas de 10: %d" % (notas_dez))
    if notas_cinco > 0:
        print("Notas de 5: %d" % (notas_cinco))
    if notas_um > 0:
        print("Notas de 1: %d" % (notas_um))
