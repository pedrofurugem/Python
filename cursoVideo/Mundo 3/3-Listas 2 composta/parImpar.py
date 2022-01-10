lista = list() #ou lista = [[], []]
par = list()
impar = list()
for c in range(1, 8):
    n = int(input(f'digite o {c}° número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(lista[:])
    elif n % 2 == 1:
        impar.append(lista[:])
    lista.clear()
print(f'lista de pares = {sorted(par)}')
print(f'lista de impares = {sorted(impar)}')
#####OU#####
'''lista = [[], []]
for c in range(1, 8): 
    n = int(input(f'digite o {c}° valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'lista de pares: {lista[0]}')
print(f'lista de pares: {lista[1]}')'''