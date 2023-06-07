''''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, 
conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
'''

numero = int(input("digite um numero inteiro:\n"))
comeco = int(input("Por qual numero você quer começar a tabuada?\n"))
fim = int(input("Em qual numero você quer parar a tabuada?\n"))
if comeco <= fim:
    for n in range(comeco, fim+1):
        tabuada = numero*n
        print("%d X %d = %d" % (numero, n, tabuada))
else:
    print("O começo deve ser MENOR que o FIM !!!")
