n = int(input('digite um número para calcular o fatorial: ')) 
cont = n  # associar a vriável ao contador
fat = 1
while cont > 0:
    print(cont, end = ' ')
    fat *= cont
    cont -= 1
print(' ')
print('{}! = {}'.format(n, fat))  
