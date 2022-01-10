time = []
jogador = {}
partidas = []
soma = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['partidas'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if opcao == 'N': 
        break
print('-=' * 30)
#cabeçario
print('cod ', end='')
for i in jogador.keys(): 
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values(): 
        print(f'{str(d):<15}', end='')
    print()
print('-' *40)
#estatiticas de um jogador em específico
while True:
    busca = int(input('digite o codigo do jogador para mostrar os dados ou 999 para sair do programa: '))
    if busca == 999:
        break 
    if busca >= len(time):
        print('Não tem jogador com esse código')
    else: 
        print(f' === LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} === ')
        for  i, g in enumerate(time[busca]['gols']): 
            print(f' No jogo {i+1} fez {g} gols')
        print('-' *40)
print('FIM')