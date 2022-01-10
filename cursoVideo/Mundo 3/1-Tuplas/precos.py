lista = ('Lapis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90
         )
print('-' *40)
print('            LISTAGEM PREÇOS           ')
print('-' *40)
for t in range(0, len(lista)): #um contador para o tamanho da listagem
    if t % 2 == 0:
        print(f'{lista[t]:.<29}', end=' ')
    else:  
        print(f'R$ {lista[t]:>7.2f}')
print('-' *40)