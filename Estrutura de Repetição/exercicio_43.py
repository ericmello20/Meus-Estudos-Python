'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''
print("O cardápio de uma lanchonete é o seguinte:")
print("Especificação   Código  Preço")
print("Cachorro Quente 100     R$ 1,20")
print("Bauru Simples   101     R$ 1,30")
print("Bauru com ovo   102     R$ 1,50")
print("Hambúrguer      103     R$ 1,20")
print("Cheeseburguer   104     R$ 1,30")
print("Refrigerante    105     R$ 1,00")

quantidade_cachorro_quente = 0
quantidade_bauru_simples = 0
quantidade_bauru_com_ovo = 0
quantidade_hamburguer = 0
quantidade_cheeseburguer = 0
quantidade_refrigerante = 0

while True:
    codigo = int(input("Digite o código do produto: (Digite 0 para encerrar a compra)\n"))

    if codigo == 0:
        break

    elif codigo < 100 or codigo > 105:
        print("Código inválido!")
        continue

    quantidade = int(input("Digite a quantidade:\n"))

    if codigo == 100:
        quantidade_cachorro_quente += quantidade
    elif codigo == 101:
        quantidade_bauru_simples += quantidade
    elif codigo == 102:
        quantidade_bauru_com_ovo += quantidade
    elif codigo == 103:
        quantidade_hamburguer += quantidade
    elif codigo == 104:
        quantidade_cheeseburguer += quantidade
    elif codigo == 105:
        quantidade_refrigerante += quantidade

valor_total = 0

if quantidade_cachorro_quente > 0:
    valor_cachorro_quente = quantidade_cachorro_quente*1.20
    valor_total += valor_cachorro_quente
    print("Cachorro quente: %d unidades pedidas.  Valor: R$%.2f" %(quantidade_cachorro_quente, valor_cachorro_quente))

if quantidade_bauru_simples > 0:
    valor_bauru_simples = quantidade_bauru_simples*1.30
    valor_total += valor_bauru_simples
    print("Bauru Simples: %d unidades pedidas.  Valor: R$%.2f" %(quantidade_bauru_simples, valor_bauru_simples))

if quantidade_bauru_com_ovo > 0:
    valor_bauru_com_ovo = quantidade_bauru_com_ovo*1.50
    valor_total += valor_bauru_com_ovo
    print("Bauru com Ovo: %d unidades pedidas.  Valor: R$%.2f" %(quantidade_bauru_com_ovo, valor_bauru_com_ovo))

if quantidade_hamburguer > 0:
    valor_hamburguer = quantidade_hamburguer*1.20
    valor_total += valor_hamburguer
    print("Hamburguer: %d unidades pedidas.  Valor: R$%.2f" %(quantidade_hamburguer, valor_hamburguer))

if quantidade_cheeseburguer > 0:
    valor_cheeseburguer = quantidade_cheeseburguer*1.30
    valor_total += valor_cheeseburguer
    print("Cheeseburguer: %d unidades pedidas.  Valor: R$%.2f" %(quantidade_cheeseburguer, valor_cheeseburguer))

if quantidade_refrigerante > 0:
    valor_refrigerante = quantidade_refrigerante*1.00
    valor_total += valor_refrigerante
    print("Regrigerante: %d unidades pedidas.  Valor: R$%.2f" %(quantidade_refrigerante, valor_refrigerante))

print("Valor Total do pedido: R$%.2f" % (valor_total))
