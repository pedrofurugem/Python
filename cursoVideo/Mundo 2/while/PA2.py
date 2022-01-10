'''
a1 = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razão da PA: '))
an = a1 + (10 -1) * r
for c in range(a1, an + r, r): 
    print(c)'''

# com while
print('PROGRESSÃO ARITIMÉTICA - PA')
a1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão da PA: '))
t = a1 #os termos começam em a1
cont = 1 #contar termos até 10
while cont <= 10:
    print('{} - '.format(t), end=' ')
    t += r #contar termo + a razão
    cont += 1 # contandor te termos
print('FIM DA P.A')
    