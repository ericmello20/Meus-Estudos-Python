"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

salario=float(input("Digite o salário do colaborador:\n"))
if salario<=280:
    reajuste=salario*0.20
    salario_ajustado=reajuste+salario
    print("Salário antes do reajuste: R$%.2f"%(salario))
    print("Percentual de aumento aplicado: 20%")
    print("Valor do aumento: R$%.2f"%(reajuste))
    print("Novo salário: R$%.2f"%(salario_ajustado))
elif 280<salario<=700:
    reajuste=salario*0.15
    salario_ajustado=reajuste+salario
    print("Salário antes do reajuste: R$%.2f"%(salario))
    print("Percentual de aumento aplicado: 15%")
    print("Valor do aumento: R$%.2f"%(reajuste))
    print("Novo salário: R$%.2f"%(salario_ajustado))
elif 700<salario<1500:
    reajuste=salario*0.10
    salario_ajustado=reajuste+salario
    print("Salário antes do reajuste: R$%.2f"%(salario))
    print("Percentual de aumento aplicado: 10%")
    print("Valor do aumento: R$%.2f"%(reajuste))
    print("Novo salário: R$%.2f"%(salario_ajustado))
elif 1500<=salario:
    reajuste=salario*0.05
    salario_ajustado=reajuste+salario
    print("Salário antes do reajuste: R$%.2f"%(salario))
    print("Percentual de aumento aplicado: 5%")
    print("Valor do aumento: R$%.2f"%(reajuste))
    print("Novo salário: R$%.2f"%(salario_ajustado))

