'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''
numero = int(input("Digite um numero:\n"))
fatorial = 1
string = "%d!" % (numero)+" = "
for n in range(numero, 1, -1):
    fatorial *= n
    string += str(n)+" . "
print(string+"1 = %d" % (fatorial))
