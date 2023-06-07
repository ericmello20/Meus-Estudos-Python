'''Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.'''

termo=int(input("Digite a quantidade de termos, para que seja calculado o valor de H: "))
denominador=1
h=0
for n in range(1,termo+1):
    h+=1/n
print("O valor de H é: %.4f"%(h))
