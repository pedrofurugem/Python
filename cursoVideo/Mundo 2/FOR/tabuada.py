n = int(input('digite um numero para tabuada: '))
for c in range(1, 10+1):
        t = n * c
        print('{} X {} = {}'.format(n, c, t))

#outra forma sem precisar de variável
#print('{} X {} = {}'.format(n, c, n*c))