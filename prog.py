import os

def clientes():
    cont=0
    # print("Escolha uma função do sistema\n(1)-Cadastro\n(2)-Exclusão\n(3)-Alteração\n(4)-Relatorio")
    while True:
        print("\n++++ Cadastro oficina ++++\nInsira seus dados corretamente abaixo")

        while True:
                nome= input("\nNome: ")
                if nome.isalpha():
                    break
                else:
                    print("Digite apenas palavras.")
                
        while True:
            try:
                idade= int(input("Idade: "))
                break
            except ValueError:
                print("Digite uma idade válida (número inteiro)")

        while True:
            cpf= input("Cpf: ")
            if (cpf.isdigit() and len(cpf)==11):
                break
            else:
                print("Digite um CPF válido.")

        while True:
            email= input("Email: ")
            if '@' in email and email.count("@")==1:
                break
            else:
                print("Digite um email válido")

        while True: 
            try: 
                telefone=input("Telefone: ")
                if telefone.isdigit() and len(telefone)==11:
                    break
                else:
                    print("Número de telefone inválido.Digite o número por extenso ex:67990028922")
            except ValueError:
                print("Número de telefone inválido.Digite o número por extenso ex:67990028922")
   
    
        print(f"\nCadastro realizado com sucesso!\nNome: {nome}\nIdade: {idade}\nCPF: {cpf}\nEmail: {email}\nTelefone: {telefone}")
        cont+=1
        while True:
            try:
                op= int(input("\nDeseja continuar\n(1)-Sim\n(0)-Não "))
                if op in [0,1]:
                    os.system('cls')
                    break
                else:
                    print("Opção inválida. Por favor, digite 1 para sim ou 0 para não.")
            except ValueError:
                print("Opção inválida. Por favor, digite 1 para sim ou 0 para não.")
        if (op==0):
            print("\nFim")
            break
           
        













# cadastro
# exclusao
# alteracao
# relatorio





# def pecas():

# def serviços():

# def contaPagar():

# def veiculos():

# def fornecedor():