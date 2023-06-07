#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

#RESOLVI USANDO WHILE MAS NÃO GOSTEI (NÃO SEI SE DÁ PRA APRIMORAR ISSO AÍ) !!!
'''
num1=int(input("digite o primeiro numero:\n"))
num2=int(input("digite o segundo numero:\n"))

if num1<num2:
    num1+=1
else:
    num2+=1

while num1<num2:    
    print(num1)
    num1+=1

while num2<num1:
    print(num2)
    num2+=1
    '''

#RESOLUÇÃO USANDO FOR:

num1=int(input("digite o primeiro numero:\n"))
num2=int(input("digite o segundo numero:\n"))

for n in range (num1+1,num2):
    print(n)
for n in range (num2+1,num1):
    print(n)
