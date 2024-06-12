def valorPagamento():
        if (dias_Atraso==0):
            return valor_Prest
        else:
            multa= valor_Prest * 0.03
            juros_Atraso= valor_Prest * (0.001*dias_Atraso)
            total=juros_Atraso + multa + valor_Prest
            return total

relatorio=0 
prestacoes=0
while True:
        valor_Prest= float(input("\nValor a ser pago: R$ "))
        dias_Atraso= int(input("Quantos dias em atraso? "))

        print('Sua conta ficou {0} dias atrasada\nTotal a pagar: R$'.format(dias_Atraso),valorPagamento())

        prestacoes+=1
        relatorio+=valorPagamento()

        inicio=int(input("\n1-para continuar a calcular\n0- para finalizar "))
        if(inicio==0):
                print('Fim.')
                print("\nForam pagas: {0} prestações\nO valor total das prestações é: R$ {1:.2f}".format(prestacoes,relatorio))
                break