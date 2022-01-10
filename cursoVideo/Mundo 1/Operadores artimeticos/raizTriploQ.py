#crie um algoritimo que leia o dobro, triplo e raiz quadrada

n = int (input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))                     #pular 2 casas
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))