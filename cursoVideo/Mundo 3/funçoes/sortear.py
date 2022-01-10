from random import randint

def sorteia(lista):
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(f'Os números sorteados foram {lista}')

def somaPar(lista):
    soma = cont = 0
    for c in lista:
        if c % 2 == 0:
            cont += 1
            soma += c
    print(f'Ao todo são {cont} pares e a soma de todos os pares é {soma}')
    
#Programa princípal - aqui determina o compartilhamento de listas
numeros = list()
sorteia(numeros)
somaPar(numeros)
