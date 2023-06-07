"""Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 

O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

valor_hora = float(input("digite o valor da sua hora:\n"))
horas_trabalhadas = int(
    input("digite quantas horas foram trabalhadas no mês:\n"))

bruto = valor_hora*horas_trabalhadas

if bruto <= 900:
    ir = "isento"
    imposto_renda = 0

elif 900 < bruto <= 1500:
    ir = "5%"
    imposto_renda = 0.05*bruto


elif 1500 < bruto <= 2500:
    ir = "10%"
    imposto_renda = 0.10*bruto

else:
    ir = "20%"
    imposto_renda = 0.20*bruto

inss = bruto*0.10
fgts = bruto*0.11
total_descontos = imposto_renda+inss
liquido = bruto-total_descontos

print("Salário Bruto   : R$%.2f" % (bruto))
print("(-) IR (%s) : R$%.2f" % (ir, imposto_renda))
print(f"(-) INSS (10%)  : R${inss}")
print(f"(-) FGTS (11%)  : R${fgts}")
print("Total Descontos : R$%.2f" % (total_descontos))
print("Salário Líquido : R$%.2f" % (liquido))
