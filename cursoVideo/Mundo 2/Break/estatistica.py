#quase la
totalCompra = Produto1000 = contPreco = menor = 0
nomeProdutoBarato = ''
while True:
    produto = str(input('informe o nome do produto: '))
    preco = float(input('informe o preço do produto: R$ '))
    totalCompra += preco
    contPreco += 1
    if preco > 1000.00:
        Produto1000 += 1
    if contPreco == 1 or preco < menor:
        menor = preco 
        nomeProdutoBarato = produto
    #ou
    '''if contPreco == 1:
        menor = preco 
        nomeProdutoBarato = produto'''
    '''else: 
        if preco < menor:
           menor = preco
           nomeProdutoBarato = produto'''
    opcao = ' '
    while opcao not in 'SsNn': # tenho que informar as duas opções dentro do while
       opcao = str(input('deseja continuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'O total gasto foi de R${totalCompra:.2f}')
print(f'{Produto1000} produtos custam acima de R$1000,00')
print(f'O produto mais barato foi {nomeProdutoBarato}')