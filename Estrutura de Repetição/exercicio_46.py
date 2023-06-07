'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome 
e as cinco distâncias alcançadas pelo atleta em seus saltos 
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. 
Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

while True:
    lista_saltos = []
    lista_ordem_saltos = ["Primeiro", "Segundo","Terceiro", "Quarto", "Quinto"]
    nome = input("Digite o nome do atleta ou ENTER para encerrar o programa:\n")

    if nome == "":
        break

    else:
        for n in range(1, 6):
            salto = float(input("Digite a distância do salto %d:\n" % (n)))
            lista_saltos.append(salto)

        lista_saltos_organizada = sorted(lista_saltos)
        
        del (lista_saltos_organizada[4])
        del (lista_saltos_organizada[0])

        media = sum(lista_saltos_organizada)/3

        print("Atleta: %s\n" % (nome))

        for i in range(0, 5):
            print("%s salto: %.2f m" %
                  (lista_ordem_saltos[i], lista_saltos[i]))

        print("\nMelhor Salto:", max(lista_saltos))
        
        print("Pior Salto:", min(lista_saltos))
        
        print("Media dos demais saltos:", media)
        
        print("Resultado final:\n%s: %.2f m" % (nome, media))
