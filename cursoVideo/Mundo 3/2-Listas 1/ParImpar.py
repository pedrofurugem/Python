lista = []
contpar = []
contimpar = []
while True:
    n = int(input('digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        contpar.append(n)
    elif n % 2 == 1:
        contimpar.append(n)
    opcao = str(input('Quer cotinuar? [S/N]: ')).upper().strip()[0]
    if opcao in 'Nn':
        break
print(f'lista original: {lista}')
print(f'lista de pares: {contpar}')
print(f'lista de impares: {contimpar}')