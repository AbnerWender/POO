client_data={}

def cadastro():
    cont=0

    while True:
        print("\n++++ Cadastro oficina ++++\nInsira seus dados corretamente abaixo")

        while True:
                nome= input("\nNome: ")
                if nome.replace(" ","").isalpha():
                    nome= nome.capitalize()
                    break
                else:
                    print("Digite apenas palavras.")
                
        while True:
            try:
                idade= int(input("Idade: "))
                if (idade <= 0 or idade >= 150):
                    print("Idade inválida.")
                else:
                    break
            except ValueError:
                print("Digite uma idade válida.")

        while True:
            cpf= input("Cpf: ")
            if (cpf.isdigit() and len(cpf)==11):
                break
            else:
                print("CPF inválido.")

        while True:
            email= input("Email: ")
            if '@' in email and email.count("@")==1:
                break
            else:
                print("Email inválido")

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
                
        client_data['Cliente']=nome
        client_data['Idade']=idade
        client_data['CPF']=cpf
        client_data['Email']=email
        client_data['Telefone']=telefone
        
        print(client_data)
        cont+=1
        while True:
            try:
                op= int(input("\nDeseja continuar\n(1)-Sim\n(0)-Não "))
                if op in [0,1]:
                    break
                else:
                    print("Opção inválida. Por favor, digite 1 para sim ou 0 para não.")
            except ValueError:
                print("Opção inválida. Por favor, digite 1 para sim ou 0 para não.")
        if (op==0):
            print("\nFim")
            break


def exclusao():
    
    while True:
        print('\nQual cliente você deseja exluir? ')
        try:
            excluir_cliente=input("Digite o nome do cliente: ")
            excluir_cliente=excluir_cliente.capitalize()
             
            if (excluir_cliente in client_data):
                del client_data[excluir_cliente]
                print(client_data)
                print("Cliente excluido com sucesso.")
                break
            else:
                print(f"{excluir_cliente} não está presente no sistema.")
        except:
            continue


    
# def altercao():

#  def relatorio():
