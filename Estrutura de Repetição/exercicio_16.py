# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

anterior = 0
atual = 1
n_termo = 1

while n_termo <= 500:
    print(n_termo)
    n_termo = atual+anterior
    anterior = atual
    atual = n_termo

print(n_termo)
