# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Na matemática, os números de Fibonacci são uma sequência ou sucessão definida como recursiva pela fórmula:
# F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Digite o termo a ser calculado:\n"))
anterior = 0
atual = 1
n_termo = 1

for i in range(1, n+1):
    print(n_termo)
    n_termo = atual+anterior
    anterior = atual
    atual = n_termo
