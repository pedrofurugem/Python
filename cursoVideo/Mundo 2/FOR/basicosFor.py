for c in range(0, 6):
    print('oi')
print('FIM')

for c in range(1, 7):
    print(c)
print('FIM')

for c in range(6, 0, -1): #conta de traz pra frente com -1
    print(c)
print('FIM')

for c in range(0, 7, 2): #pula duas casas
    print(c)
print('FIM')

for c in range(7, 0, -2): #pula duas casas de traz pra frente
    print(c)
print('FIM')

n = int(input('Digite um numero: '))
for c in range(0, n+1): #pra chegar ao numero
    print(c)
print('FIM')


i = int(input('Ínicio: ')) #inicio
f = int(input('Fim: ')) #fim
p = int(input('Passo: ')) #passo
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3): #pede para escrever varias vezes um valor
   n = int(input('digite um valor: '))
print('fim')

for c in range(0, 3): #pede para escrever varias vezes um valor
   n = int(input('digite um valor: '))
print('fim')

s = 0
for c in range(0, 4): 
    n = int(input('Digite um valor: '))
    s += n # += somatorio dos valores
print('O somatorio de todos os valores foi {}'.format(s))
