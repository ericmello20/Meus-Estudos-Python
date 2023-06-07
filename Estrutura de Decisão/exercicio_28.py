'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

tipo_carne = input("Digite o tipo de carne que irá comprar: \nFile Duplo\nAlcatra\nPicanha\n")
quantidade_carne = float(input("Digite a quantidade de carne que irá comprar:\n"))
tipo_pagamento = input("Digite o meio de pagamento:\n")

preco_file_ate_5kg = 4.90*quantidade_carne
preco_alcatra_ate_5kg = 5.90*quantidade_carne
preco_picanha_ate_5kg = 6.90*quantidade_carne

preco_file_acima_5kg = 5.80*quantidade_carne
preco_alcatra_acima_5kg = 6.80*quantidade_carne
preco_picanha_acima_5kg = 7.80*quantidade_carne

print("Tipo da Carne: %s" % (tipo_carne))
print("Quantidade de Carne: %.2fkg" % (quantidade_carne))

if tipo_carne == "File Duplo":
    if quantidade_carne <= 5:
        total = preco_file_ate_5kg
    else:
        total = preco_file_acima_5kg

if tipo_carne == "Alcatra":
    if quantidade_carne <= 5:
        total = preco_alcatra_ate_5kg
    else:
        total = preco_alcatra_acima_5kg

if tipo_carne == "Picanha":
    if quantidade_carne <= 5:
        total = preco_picanha_ate_5kg
    else:
        total = preco_picanha_acima_5kg

if tipo_pagamento == "cartão tabajara":
    desconto = total*0.05
    preco_com_desconto = total-desconto
    print("Preço Total: R$%.2f" % (total))
    print("Tipo de Pagamento: %s" % (tipo_pagamento))
    print("Valor do Desconto: R$%.2f" % (desconto))
    print("Total a Pagar: R$%.2f" % (preco_com_desconto))
else:
    desconto = 0
    print("Preço Total: R$%.2f" % (total))
    print("Tipo de Pagamento: %s" % (tipo_pagamento))
    print("Valor do Desconto: R$%.2f" % (desconto))
    print("Total a Pagar: R$%.2f" % (total))
