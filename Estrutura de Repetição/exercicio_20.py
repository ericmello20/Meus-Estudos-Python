# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.


quantidade = int(input("deseja calcular o fatorial de quantos números?\n"))

contador = 0

while contador < quantidade:
    numero = float(input(
        "digite o número para o cálculo do fatorial (inteiro, positivo e menor do que 16):\n"))

    if numero > 16 or numero < 0:
        print("numero inválido!")

    else:
        fatorial = 1

        for i in range(1, numero+1):
            fatorial *= i
    print(fatorial)
    contador += 1
