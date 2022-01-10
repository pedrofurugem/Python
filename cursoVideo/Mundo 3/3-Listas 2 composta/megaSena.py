#REFAZE
from random import randint 
from time import sleep
lista = []
jogos = []
qtd = int(input('Quantos jogos?: '))
total = 0
while total <= qtd:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' *30)
print('  MEGA SENA  ')
for i, l in enumerate(jogos):
    sleep(1)
    print(f'  jogo {i+1}: {l}')
print('-=' *12,'BOA SORTE', '-=' *12)

