'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''
termo = int(input("Digite o n termo da série, para que seja efetuado o cálculo: "))


denominador = 1
soma_serie = 0
string = "S = "

for n in range(1, termo+1):
    s = n/denominador
    soma_serie += s
    if n < termo:
        string += (f"{n}")+"/"+(f"{denominador}")+" + "
    elif n == termo:
        string += (f"{n}")+"/"+(f"{denominador}")
    denominador += 2

print(string)
print("Resultado da soma da série: %.4f" % (soma_serie))
