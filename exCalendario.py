meses=['Janeiro','Fevereiro','Março','Abeil','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
def calendario():
    data=input('Insira a data\nDD/MM/AAAA: ')
    if data[2] !='/' or data[5]!='/' or len(data)!= 10:
        print("Data inválida")
    else:
        print(data[:2]+' de '+meses[0]+' de '+data[6:])  # o mes sempre será janeiro, pois 'meses[0]' define isso.


calendario()