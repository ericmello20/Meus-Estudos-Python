'''Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

print("PARA VOTAR NO CANDIDATO 1 - DIGITE: 1\nPARA VOTAR NO CANDIDATO 2 - DIGITE: 2\nPARA VOTAR NO CANDIDATO 3 - DIGITE: 3")
num_eleitores = int(input("Digite o numero de eleitores:\n"))
candidato1 = 0
candidato2 = 0
candidato3 = 0
for n in range(1, num_eleitores+1):
    voto = int(input("Digite em quem você vai votar: (1, 2 ou 3)\n"))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1

print("O candidato 1 teve %d votos" % (candidato1))
print("O candidato 2 teve %d votos" % (candidato2))
print("O candidato 3 teve %d votos" % (candidato3))
