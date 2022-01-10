#n = int(input('digite um numero: '))
#if n % 2 == 1 and n % 3 == 1: 
#    print('é primo')
#else: 
 #   print('não é primo')

#refazer
print('---NÚMEROS PRIMOS---')
n = int(input('digite um número: '))
cont = 0
for c in range(1, n+1, 1):
    print(c, end = ' ')
    if n % c == 0:
        cont += 1
print(' ')
print('{} foi divisivel {} vezes'.format(n, cont))
if cont == 2:
    print('portanto é primo')
else:
    print('portanto não é primo')

