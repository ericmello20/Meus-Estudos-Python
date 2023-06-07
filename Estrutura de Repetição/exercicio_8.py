#Faça um programa que leia 5 números e informe a soma e a média dos números.

#APRIMOREI O PROGRAMA PARA SER UTILIZADO COM QUALQUER QUANTIDADE DE NUMEROS QUE O USUÁRIO QUISER!

n=int(input("digite a quantidade de numeros para que quer calcular: "))
soma=0
for num in range(n):
    numero=float(input("digite o numero: "))
    soma+=numero
media=soma/5
print("A soma é: %.2f\nA média é: %.2f"%(soma, media))

#O PROGRAMA ORIGNIAL (COMO PEDE O ENUNCIADO) SERIA:
#soma=0
#for num in range(5):
#    numero=float(input("digite o numero: "))
#    soma+=numero
#media=soma/5
#print("A soma é: %.2f\nA média é: %.2f"%(soma, media))
