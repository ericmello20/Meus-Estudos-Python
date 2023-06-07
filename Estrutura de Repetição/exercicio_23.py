'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''

lista_primos = []
numero = int(input("digite um numero inteiro!\n"))
testes = 0


if numero < 2:
    print("Não há números primos!!")

elif numero >= 2:
    
    lista_primos.append(2)

    for n in range(3, numero+1,2):
        contador = 0

        for i in range(1, n+1):

            if n % i == 0:

                contador += 1
    
        testes+=1

        if contador == 2:
            lista_primos.append(n)

    print("De 0 até %d, temos como números primos:\n%r"%(numero,lista_primos))
    print("Foram feitos %d testes para chegar a este resultado"%(testes))
