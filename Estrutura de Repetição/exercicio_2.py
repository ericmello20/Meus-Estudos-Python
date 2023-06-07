# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("digite um nome de usuario:\n")
senha = input("digite uma senha\n")
while usuario == senha:
    print("erro, nome de usuário e senha iguais.\ndigite novamente!")
    usuario = input("digite um nome de usuario:\n")
    senha = input("digite uma senha:\n")
print("usuário e senha válidos!")
