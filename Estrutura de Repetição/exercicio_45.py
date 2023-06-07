'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova 
e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 

Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''
lista_gabarito = []
lista_acertos = []
quantidade_alunos = 0
soma_notas = 0

print("Olá, professor, digite o gabarito da sua prova!")

for n in range(1, 11):
    gabarito = input("Qual o gabarito da pergunta %d? " % (n)).upper()
    lista_gabarito.append(gabarito)

print("Boa Prova, Aluno!")

fazer_prova = "S"

while fazer_prova == "S":
    pontuacao = 0

    for i in range(1, 11):
        resposta = input("Qual a resposta correta da pergunta %d?" % (i)).upper()

        if i == 1 and resposta == lista_gabarito[0]:
            pontuacao += 1
        elif i == 2 and resposta == lista_gabarito[1]:
            pontuacao += 1
        elif i == 3 and resposta == lista_gabarito[2]:
            pontuacao += 1
        elif i == 4 and resposta == lista_gabarito[3]:
            pontuacao += 1
        elif i == 5 and resposta == lista_gabarito[4]:
            pontuacao += 1
        elif i == 6 and resposta == lista_gabarito[5]:
            pontuacao += 1
        elif i == 7 and resposta == lista_gabarito[6]:
            pontuacao += 1
        elif i == 8 and resposta == lista_gabarito[7]:
            pontuacao += 1
        elif i == 9 and resposta == lista_gabarito[8]:
            pontuacao += 1
        elif i == 10 and resposta == lista_gabarito[9]:
            pontuacao += 1

    soma_notas += pontuacao

    lista_acertos.append(pontuacao)

    quantidade_alunos += 1

    fazer_prova = input("Outro aluno irá fazer a prova? (S ou N)").upper()

media_notas = soma_notas/quantidade_alunos

print(f"O maior acerto foi: {max(lista_acertos)}")
print(f"O menor acerto foi: {min(lista_acertos)}")
print(f"O sistema foi utilizado por {quantidade_alunos} alunos")
print("A média das notas da turma foi: %.2f"%(media_notas))
print(">>> GABARITO <<<")

for n in lista_gabarito:
    print(list(n))
