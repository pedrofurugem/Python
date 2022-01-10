from random import randint
cont = maior = menor= 0
n = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
print('Os valores sorteados foram:')
for c in n:
    print(f'{c}', end= ' ')
print(' ')
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')