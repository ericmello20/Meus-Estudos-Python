'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 

Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...

'''

print("Digite 0 para encerrar a compra!")

lista_preco=[]
total = 0
produto = 0
#ideia: percorrer lista para pegar os preços dos produtos!
lista_precos=[]
while True:
    preco = float(input("Digite o valor do produto:\n"))
    
    if preco != 0:
        lista_preco.append(preco)
        total += preco
        produto += 1
    else:
        break

dinheiro = float(input("Digite o valor em dinheiro:\n"))
troco = dinheiro-total

for n in range(1, produto+1):
    print("Produto %d: R$%.2f" % (n, lista_preco[n-1]))

print("Total: R$%.2f" % (total))

print("Dinheiro: R$%.2f" % (dinheiro))

print("Troco: R$%.2f" % (troco))
