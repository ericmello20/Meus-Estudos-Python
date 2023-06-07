'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes
'''

codigo_mais_magro = 0
peso_mais_magro = 1000

codigo_mais_gordo = 0
peso_mais_gordo = 0

codigo_mais_baixo = 0
altura_mais_baixo = 500

codigo_mais_alto = 0
altura_mais_alto = 0

soma_altura = 0
soma_peso = 0
quantidade_clientes = 0

while True:

    codigo = int(input("Digite o código do cliente:\n"))

    if codigo == 0:
        break

    quantidade_clientes += 1

    peso_cliente = float(input("Digite o peso do cliente:\n"))
    altura_cliente = float(input("Digite a altura do cliente:\n"))

    soma_peso += peso_cliente
    soma_altura += altura_cliente

    if peso_cliente > peso_mais_gordo:
        peso_mais_gordo = peso_cliente
        codigo_mais_gordo = codigo

    if altura_cliente > altura_mais_alto:
        altura_mais_alto = altura_cliente
        codigo_mais_alto = codigo

    if peso_cliente < peso_mais_magro:
        peso_mais_magro = peso_cliente
        codigo_mais_magro = codigo

    if altura_cliente < altura_mais_baixo:
        altura_mais_baixo = altura_cliente
        codigo_mais_baixo = codigo

media_pesos = soma_peso/quantidade_clientes
media_alturas = soma_altura/quantidade_clientes

print("Cliente mais alto >>> Código: %d >>> Altura: %.2f" %(codigo_mais_alto, altura_mais_alto))
print("Cliente mais baixo >>> Código: %d >>> Altura: %.2f" %(codigo_mais_baixo, altura_mais_baixo))
print("Cliente mais gordo >>> Código: %d >>> Peso: %.2f" %(codigo_mais_gordo, peso_mais_gordo))
print("Cliente mais magro >>> Código: %d >>> Peso: %.2f" %(codigo_mais_magro, peso_mais_magro))
print("Média dos Pesos: %.2f\nMédia das alturas: %.2f" %(media_pesos, media_alturas))
