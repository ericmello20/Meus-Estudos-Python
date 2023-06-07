'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

ano_atual = int(input("Qual é o ano atual?\n"))

salario = float(input("Digite o salário inicial:\n"))

percentual_aumento = 0.015

for n in range(1996, ano_atual+1):
    salario = salario+(percentual_aumento*salario)
    percentual_aumento *= 2

print("O salário atual é: %.2f" % (salario))
