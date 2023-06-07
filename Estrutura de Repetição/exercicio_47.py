'''Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. 
A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação 
e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informados ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04'''

while True:
    lista_notas = []
    nome = input("Digite o nome do atleta:\nAVISO: Se não houver nome, o programa será interrompido\n")

    if nome == "":
        break

    else:
        for n in range(1, 8):
            nota = float(
                input("Olá, jurado, digite a nota que você dá ao atleta: "))
            lista_notas.append(nota)

        lista_notas_organizada = sorted(lista_notas)

        del (lista_notas_organizada[6])
        del (lista_notas_organizada[0])

        media = sum(lista_notas_organizada)/5

        print("Atleta: %s" % (nome))
        
        for i in range(0, 7):
            print("Nota: %.2f" % (lista_notas[i]))
        
        print("\nResultado final:\nAtleta: %s" % (nome))
        
        print("Melhor nota: %.2f\nPior nota: %.2f\nMedia: %.2f" %(max(lista_notas), min(lista_notas), media))
