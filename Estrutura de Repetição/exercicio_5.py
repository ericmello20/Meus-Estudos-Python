# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

repetir = "S"

while repetir in "sS":

    populacaoA = int(input("digite a população da cidade A\n"))
    populacaoB = int(input("digite a população da cidade B\n"))
    crescimentoA = float(
        input("digite a taxa de crescimento da cidade A\n"))/100
    crescimentoB = float(
        input("digite a taxa de crescimento da cidade B\n"))/100

    if populacaoA == populacaoB:
        print("população com valores iguais!!! digite valores diferentes")
    elif populacaoA < populacaoB and crescimentoA < crescimentoB:
        print("A população A nunca ultrapassará a população B!")
    elif populacaoB < populacaoA and crescimentoB < crescimentoA:
        print("A população B nunca ultrapassará a população A!")

    ano = 0

    while (populacaoA < populacaoB and crescimentoA > crescimentoB) or (populacaoB < populacaoA and crescimentoB > crescimentoA):
        populacaoA += populacaoA*crescimentoA
        populacaoB += populacaoB*crescimentoB
        ano += 1
        print("Foram necessários %d anos." % (ano))
        print("População A: %d" % (populacaoA))
        print("População B: %d" % (populacaoB))

    repetir = input("gostaria de repetir a operação (S ou N)?\n")

print("até a próxima!")
