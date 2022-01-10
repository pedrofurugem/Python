lista = list()
while True:
    n = int(input('adicione um numero ')) 
    if n not in lista:
        lista.append(n)
    else:
        print('numero repetido')
    while True:    
        opcao = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao in 'N':
        break
print(sorted(lista))
       