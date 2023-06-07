#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra=input("Digite \"F\" para Feminino ou \"M\" para Masculino:\n")
if letra=="F":
    print("Feminino")
elif letra=="M":
    print("Masculino")
else:
    print("Sexo Inválido")