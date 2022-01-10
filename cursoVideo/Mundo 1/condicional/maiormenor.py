#meu jeito de fazer
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

if n1 > n2 and n1 > n3 and n2 > n3:
   print('{} é o maior'.format(n1))
   print('{} é o menor'.format(n3))
if n1 > n2 and n1 > n3 and n3 > n2:
   print('{} é o maior'.format(n1))
   print('{} é o menor'.format(n2))
if n2 > n1 and n2 > n3 and n1 > n3:
   print('{} é o maior'.format(n2))
   print('{} é o menor'.format(n3))
if n2 > n1 and n2 > n3 and n3 > n1:
   print('{} é o maior'.format(n2))
   print('{} é o menor'.format(n1))
if n3 > n1 and n3 > n2 and n2 > n1:
   print('{} é o maior'.format(n3))
   print('{} é o menor'.format(n1))
if n3 > n1 and n3 > n2 and n1 > n2:
    print('{} é o maior'.format(n3))
    print('{} é o menor'.format(n2))

#Guanabara
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))
#verificando menor
menor = n1
if n2<n1 and n2<n3:
   menor = n2
if n3<n1 and n3<n2:
   menor = n3 
#verificando maior
maior = n1 
if n2>n1 and n2>n3:
   maior = n2
if n3>n1 and n3>n2:
   maior = n3 
print('{} é o menor'.format(menor))
print('{} é o maior'.format(maior))