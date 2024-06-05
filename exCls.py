import os

while True:
    valor= int(input("Digite o valor 1 ou 0 para encerrar "))
    if (valor==1):
        print("valor correto")
        os.system('cls') #cls é usado para limpar o terminal
    elif (valor==0):
        print("Valor para sair")
        break
    elif(valor!=1 or valor!= 0):
        print("Valor invalido!")