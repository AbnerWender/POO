class Cliente:
    def __init__(self, nome, idade, cpf, email, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nEmail: {self.email}\nTelefone: {self.telefone}"

class Cadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self):
        while True:
            print("\n++++ Cadastro oficina ++++\nInsira seus dados corretamente abaixo")

            nome = input("\nNome: ")
            try:
                if nome.replace(" ", "").isalpha():
                    nome = nome.capitalize()
                    break
                else:
                    print("Digite apenas palavras.")
            except ValueError:
                print("Digite apenas palavras.")

        while True:
            try:
                idade = int(input("Idade: "))
                if idade <= 0 or idade >= 150:
                    print("Idade inválida.")
                else:
                    break
            except ValueError:
                print("Digite uma idade válida.")

        while True:
            cpf = input("Cpf: ")
            try:
                if cpf.isdigit() and len(cpf) == 11:
                    break
                else:
                    print("CPF inválido.")
            except ValueError:
                print("CPF inválido.")

        while True:
            email = input("Email: ")
            if '@' in email and email.count("@") == 1:
                break
            else:
                print("Email inválido")

        while True:
            try:
                telefone = input("Telefone: ")
                if telefone.isdigit() and len(telefone) == 11:
                    break
                else:
                    print("Número de telefone inválido.Digite o número por extenso ex:67990028922")
            except ValueError:
                print("Número de telefone inválido.Digite o número por extenso ex:67990028922")

        cliente = Cliente(nome, idade, cpf, email, telefone)
        self.clientes.append(cliente)
        print(f"\nCadastro realizado com sucesso!\n{cliente}")
        print(cliente)

    def continuar(self):
        while True:
            try:
                op = int(input("\nDeseja continuar\n(1)-Sim\n(0)-Não "))
                if op in [0, 1]:
                    return op
                else:
                    print("Opção inválida. Por favor, digite 1 para sim ou 0 para não.")
            except ValueError:
                print("Opção inválida. Por favor, digite 1 para sim ou 0 para não.")

# def main():
#     cadastro = Cadastro()
#     while True:
#         cadastro.cadastrar_cliente()
#         op = cadastro.continuar()
#         if op == 0:
#             print("\nFim")
#             break

# if __name__ == "__main__":
#     main()