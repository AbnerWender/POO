def calculadora():
    op=input("Qual operação matemática ?\n(+) Adição\n(-) Subtração\n(*) Multiplicaçao\n(/) Divisão ")
    x= int(input('\nDigite um valor: '))
    y= int(input('Digite outro valor: '))
    

    if (op=='+'):
        resultado = x+y
    elif (op=='-'):
        resultado=x-y
    elif (op =='*'):
        resultado= x*y
    elif (op=='/'):
        resultado= x/y
    return resultado

        
x = calculadora()
print('resultado= {0:.0f}'.format(x))