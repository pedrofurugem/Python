from random import randint
itens = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador]))

print ('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int (input('Qual é a sua jgada? '))
print('Computador jogou {}'.itens[computador])
print('jpgador jogou {}'.itens[jogador])