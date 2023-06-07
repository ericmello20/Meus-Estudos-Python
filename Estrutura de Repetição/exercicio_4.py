'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.
'''

populacaoA = 80000
populacaoB = 200000
crescimentoA = 0.03
crescimentoB = 0.015
ano = 0
while populacaoA < populacaoB:
    populacaoA += populacaoA*0.03
    populacaoB += populacaoB*0.015
    ano += 1
print("Foram necessários %d anos." % (ano))
print("População A: %d" % (populacaoA))
print("População B: %d" % (populacaoB))
