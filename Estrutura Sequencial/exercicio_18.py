'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''
tamanho = float(input("digite o tamanho do arquivo (em MB)\n"))
velocidade = float(
    input("digite a velocidade do link de internet (em Mbps)\n"))
download = (tamanho/(velocidade/8))/60
print("O tempo necessário para baixar o arquivo será %.4f minutos" % (download))
