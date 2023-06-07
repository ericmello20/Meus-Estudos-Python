'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

quantidade_morangos = int(input("Quantidade de morangos adquiridos (kg):\n"))
quantidade_macas = int(input("Quantidade de maçãs adquiridas (kg):\n"))
if quantidade_morangos <= 5:
    valor_morangos = 2.50*quantidade_morangos
else:
    valor_morangos = 2.20*quantidade_morangos
if quantidade_macas <= 5:
    valor_macas = 1.80*quantidade_macas
else:
    valor_macas = 1.50*quantidade_macas

valor_total_compra = valor_morangos+valor_macas

if quantidade_morangos+quantidade_macas > 8 or valor_total_compra > 25.00:
    desconto = valor_total_compra-(valor_total_compra*0.10)
    print("Valor total a ser pago: R$%.2f" % (desconto))
else:
    print("Valor total a ser pago: R$%.2f" % (valor_total_compra))
