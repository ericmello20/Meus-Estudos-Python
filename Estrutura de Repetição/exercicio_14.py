# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = []
impar = []
for n in range(1, 11):
    numero = int(input("digite o numero:\n"))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(len(par))
print(len(impar))

# Também poderia ser feito com contadores:
# contador_par=0
# contador_impar=0
# for n in range (1,11):
#    numero=int(input("digite o numero:\n"))
#    if numero%2==0:
#        contador_par+=1
#    else:
#        contador_impar+=1
# print(contador_par)
# print(contador_impar)
