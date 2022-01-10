#for c in range(1, 10): 
 #   print(c)
#print('Fim')
#mesma coisa

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

#While serve para quando você não sabe o limite
#Flag ponto de parada
#sempre definir por cima o começo do laço

n = 1
while n != 0:
   n = int(input('Digite um valor: '))
print('Fim')

#enquanto não digita 's'
r = 'S'
while r == 'S': 
    n = int(input('Digite uma valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')


n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0: 
            par += 1 #contagem com +!
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros ímpares'.format(par, impar))
