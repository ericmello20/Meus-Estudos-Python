'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''

print(">>>>> Responda apenas \"s\" ou \"n\" <<<<<")
telefonou=input("Você telefonou para a vítima?\n")
local=input("Esteve no local do crime?\n")
mora_perto=input("Mora perto da vítima?\n")
devia=input("Devia para a vítima?\n")
trabalhou=input("Já trabalhou com a vítima?\n")
contador=0

if telefonou=="s":
    contador+=1
if local=="s":
    contador+=1
if mora_perto=="s":
    contador+=1
if devia=="s":
    contador+=1
if trabalhou=="s":
    contador+=1

if contador==2:
    print("Suspeita")
elif 3<=contador<=4:
    print("Cúmplice")
elif contador==5:
    print("Assassino")
else:
    print("inocente")