from random import randint
from time import sleep
from operator import itemgetter #ordenar valores em um dicionário
jogador = dict()
jogador['jogador 1'] = randint(1, 6)
jogador['jogador 2'] = randint(1, 6)
jogador['jogador 3'] = randint(1, 6)
jogador['jogador 4'] = randint(1, 6)

ranking = list()
print('valores sorteados')
for k, v in jogador.items():
    sleep(1)
    print(f'{k} tirou {v}')

print('-=' *30)
print('  == RANKING DOS JOGADORES ==  ')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
#print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)