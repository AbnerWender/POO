import os

while True:
    valor= int(input("Digite o valor 1 ou 0 para encerrar "))
    if (valor==1):
        print("valor correto")
        os.system('pause') #pause simplesmente pausa o cód. e mostra uma mensagem "Pressione qualquer tecla para continuar. . ."
    elif (valor==0):
        print("Valor para sair")
        break
    elif(valor!=1 or valor!= 0):
        print("Valor invalido!")