'''
Em uma eleição presidencial existem quatro candidatos. 
Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

print("Código para votação:")
print("1 - José")
print("2 - João")
print("3 - Pedro")
print("4 - Maria")
print("5 - Voto Nulo")
print("6 - Voto em Branco")

votos_1=0
votos_2=0
votos_3=0
votos_4=0
votos_5=0
votos_6=0
total_votos=0

while True:
    codigo=int(input("Digite o código do seu candidato: (0 para encerrar o conjunto de votos)\n"))
    
    if codigo==0:
        break
    
    elif codigo<0 or codigo>6:
        print("Código inválido!")
        continue
    
    total_votos+=1
    
    if codigo==1:
        votos_1+=1
    
    elif codigo==2:
        votos_2+=1
    
    elif codigo==3:
        votos_3+=1
    
    elif codigo==4:
        votos_4+=1
    
    elif codigo==5:
        votos_5+=1
    
    elif codigo==6:
        votos_6+=1

porcentagem_nulo=(votos_5*100)/total_votos
porcentagem_branco=(votos_6*100)/total_votos

print("Candidato José: %d Votos"%(votos_1))
print("Candidato João: %d Votos"%(votos_2))
print("Candidato Pedro: %d Votos"%(votos_3))
print("Candidata Maria: %d Votos"%(votos_4))
print(f"Votos Nulo: {votos_5}  Porcentagem de Votos Nulo: {porcentagem_nulo}%")
print(f"Votos em Branco: {votos_6}  Porcentagem de Votos em Branco: {porcentagem_branco}%")

