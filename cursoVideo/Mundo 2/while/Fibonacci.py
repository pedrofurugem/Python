#fazer a transição de termos
print('-' * 30)
print('Sequência de Fibonnaci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end = ' ')
cont = 3 # cont começa em 3 porque eu ja mostrei t1 e t2
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end = ' ')
    t1 = t2 # aqui acontece a transição de termos t1 no lugar de t2
    t2 = t3 # t2 no lugar de t3
    cont += 1
print(' - FIM')