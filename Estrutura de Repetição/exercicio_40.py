'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 

Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). 

Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

maior_indice_acidentes=0
menor_indice_acidentes=99999999
codigo_maior_indice=0
codigo_menor_indice=0

soma_acidentes=0
soma_veiculos=0
cidades=5
cidades_menos_2000_acidentes=0

for n in range(1,6):
    codigo=int(input("Digite o código da cidade: "))
    numero_veiculos=int(input("Digite o numero de veiculos de passeio: "))
    numero_acidentes=int(input("Digite o numero de acidentes de trânsito com vítimas: "))
    
    soma_veiculos+=numero_veiculos

    if numero_veiculos<2000:
        soma_acidentes+=numero_acidentes
        cidades_menos_2000_acidentes+=1
    
    if numero_acidentes>maior_indice_acidentes:
        maior_indice_acidentes=numero_acidentes
        codigo_maior_indice=codigo
    
    if numero_acidentes<menor_indice_acidentes:
        menor_indice_acidentes=numero_acidentes
        codigo_menor_indice=codigo
    
media_veiculos=soma_veiculos/cidades
media_acidentes=soma_acidentes/cidades_menos_2000_acidentes

print("O maior indice de acidentes é: %d; e pertence a cidade de código: %d"%(maior_indice_acidentes,codigo_maior_indice))
print("O menor indice de acidentes é: %d; e pertence a cidade de código: %d"%(menor_indice_acidentes,codigo_menor_indice))
print("A média de veículos nas 5 cidades juntas é: %d"%(media_veiculos))
print("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é: %d"%(media_acidentes))

