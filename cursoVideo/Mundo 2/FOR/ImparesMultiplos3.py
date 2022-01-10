s = 0 #acumulador
cont = 0 #contador
for c in range (1, 500+1): 
    if c % 2 == 1 and c % 3 == 0: 
        #print(c, end=' ')
        s += c # +=formula para somar
        cont += 1 # contar todos os valores de range
print(' ')
print('A soma de todos esses valores é igual a {} e o total de numeros é {}'.format(s, cont))
