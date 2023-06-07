#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra=input("digite uma letra:\n")
if letra in "aeiouAEIOU":
    print("A letra digitada é uma vogal")
else:
    print("A letra digitada é uma consoante")