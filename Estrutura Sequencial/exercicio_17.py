"""Faça um Programa para uma loja de tintas.
 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

area_pintada = float(
    input("Digite o tamanho (em metros quadrados) da área a ser pintada:\n"))

litros = area_pintada/6
latas = litros/18
galoes = litros/3.6

if latas % 18 != 0:
    latas += 1
    preço_latas = latas*80

if galoes % 3.6 != 0:
    galoes += 1
    preço_galoes = galoes*25

mistura_lata = litros//18
mistura_galao = (litros-(mistura_lata*18))//3.6

if (litros-(mistura_lata*18)) % 3.6 != 0:
    mistura_galao += 1
    preço_mistura = (mistura_lata*80)+(mistura_galao*25)

print("Quantidade de tinta em LATAS: %d\nPreço em LATAS: %d" % (latas, preço_latas))
print("Quantidade de tinta em GALÕES: %d\nPreço em GALÕES: %d" % (galoes, preço_galoes))
print("Quantidade de tinta MISTURANDO LATAS E GALÕES: %d LATAS e %d GALÕES\nPreço MISTURANDO LATAS E GALÕES: %d" % (mistura_lata, mistura_galao, preço_mistura))
