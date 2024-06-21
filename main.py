import os
from classe import*

while True:
    print("\n++++ Menu ++++")
    print("(1) Cadastro")
    print("(2) Exclusão")
    print("(3) Alteração")
    print("(4) Relatório")
    print("(0) Sair")
    try:
        op = int(input("Opção: "))
        if op == 1:
            Cadastro.cadastrar_cliente()
        elif op == 2:
            exclusao()
        elif op == 0:
            print("\nFim")
            break
        else:
            print("Opção inválida. Por favor, digite 1 para cadastro, 2 para exclusão ou 0 para sair.")
    except ValueError:
        print("Opção inválida. Por favor, digite 1 para cadastro, 2 para exclusão ou 0 para sair.")