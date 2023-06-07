"""Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

from math import ceil
area_pintada = float(
    input("Digite o tamanho (em metros quadrados) da área a ser pintada:\n"))
quantidade_tinta = area_pintada/3
latas = ceil(quantidade_tinta/18)
preço = latas*80
print("Será necessário comprar: %d latas de tinta\n Valor total R$%.2f" % (latas, preço))
