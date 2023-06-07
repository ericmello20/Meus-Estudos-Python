# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# 5 tipos diferentes de formatação

numero = float(input("digite um numero: \n"))
print("O numero informado foi", numero)
print("O numero informado foi {}".format(numero))
print(f"O numero informado foi {numero}")
print("O numero informado foi %f" % (numero))
print("O numero informado foi "+str(numero))
