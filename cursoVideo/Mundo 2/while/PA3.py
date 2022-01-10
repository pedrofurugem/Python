# com while
print('PROGRESSÃO ARITIMÉTICA - PA')
a1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão da PA: '))
t = a1 #os termos começam em a1
cont = 1 #contar termos até 10
total = 0 
n = 10
while n != 0:
    total = total + n
    while cont <= total:
        print('{} - '.format(t), end=' ')
        t += r #contar termo + a razão
        cont += 1 # contandor te termos
    print('PAROU')
    n = int(input('Quantos termos você quer a mais: '))
print('Progressão Aritimética finalizada com {} termos:'.format(total))
    

    