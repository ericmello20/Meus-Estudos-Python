'''Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input("Qual o turno que você estuda?\n\"M\" para matutino\n\"V\" para vespertino\n\"N\" para noturno\n")

if turno == "M" or turno == "m":
    print("Bom dia!")
if turno == "V" or turno == "v":
    print("Boa tarde!")
if turno == "N" or turno == "n":
    print("Boa noite!")
