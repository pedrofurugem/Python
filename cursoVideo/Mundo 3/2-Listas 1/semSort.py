#Sem sort é complicado
lista = list()
for c in range(0, 5):
    n = int(input('adicione um número: '))
    if c == 0:   
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n) #percorrendo a lista
                break
            pos += 1 #conta + uma posição
print('-=' *30)
print(lista)