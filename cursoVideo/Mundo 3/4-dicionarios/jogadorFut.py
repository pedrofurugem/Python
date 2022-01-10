jogador = dict()
partidas = list()
jogador['nome'] = str(input('nome do jogador: '))
total = int(input(f'Quantas partidas jogou {jogador["nome"]}: '))
for g in range(0, total):
    partidas.append(int(input(f'quantos gols fez na partida {g+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('-=' * 30)
for i, v in jogador.items():
    print(f'O campo {i} tem valor {v}')
print('-=' * 30) 
print(f'O jogador {jogador["nome"]} jogou {total} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i+1} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
