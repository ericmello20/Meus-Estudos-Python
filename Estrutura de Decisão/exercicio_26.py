'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

litros=float(input("litros vendidos:\n"))
tipo_combustível=input("Digite o tipo de combustível: \n\"A\" - Para álcool\n\"G\" - Para gasolina\n")

if tipo_combustível in "Aa":
    
    alcool=1.90
    
    if litros<=20:
        litro_com_desconto=alcool-(alcool*0.03)
        valorfinal=litro_com_desconto*litros
        print("Valor Total: R$%.2f"%(valorfinal))
    
    elif litros>20:
        litro_com_desconto=alcool-(alcool*0.05)
        valorfinal=litro_com_desconto*litros
        print("Valor Total: R$%.2f"%(valorfinal))

elif tipo_combustível in "Gg":
    
    gasolina=2.50
    
    if litros<=20:
        litro_com_desconto=gasolina-(gasolina*0.04)
        valorfinal=litro_com_desconto*litros
        print("Valor Total: R$%.2f"%(valorfinal))
    
    elif litros>20:
        litro_com_desconto=gasolina-(gasolina*0.06)
        valorfinal=litro_com_desconto*litros
        print("Valor Total: R$%.2f"%(valorfinal))


