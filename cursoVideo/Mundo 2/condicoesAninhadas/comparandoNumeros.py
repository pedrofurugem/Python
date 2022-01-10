n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
print(n1)
print(n2)

if n1 > n2: 
    print('{} O primeiro valor é maior'.format(n1))
elif n2 > n1: 
    print('{} O segundo valor é maior'.format(n2))
elif n1 == n2: 
    print('não exite valor maior, os dois valores são iguais')