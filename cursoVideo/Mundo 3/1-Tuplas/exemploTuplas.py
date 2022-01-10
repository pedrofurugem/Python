"AS TUPLAS SÃO IMUTAVEIS"

#tanto faz a tupla ser com ou sem parenteses
lanche = ('Hámburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) #suco
print(lanche[-2]) #Pizza
print(lanche[1:3]) #('Suco', 'Pizza') #fatiamentos
print(lanche[2:]) #('Pizza', 'Pudim') #posição 2 pra fente
print(lanche[:2]) #('Hámburguer', 'Suco') # posição 2 para trás, ignonara o ultimo elemento
print(lanche[-2:]) #('Pizza', 'Pudim') --- ultimos elementos
print(lanche[-3:]) #('Suco', 'Pizza', 'Pudim')

#TUPLAS SÃO IMUTAVEIS
#lanche[1] = 'Refresco'
#print(lanche[1]) #TypeError: 'tuple' object does not support item assignment


'''Três formas de fazer FOR com range e variável composta // Os dois tem o mesmo resultado'''

print(' ')

#FOR com range
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

print('')
#tupla em um FOR
for comida in lanche:
   print(f'Eu vou comer {comida}')

print('')
#com enumerate, informa a posição e enumera
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
    
print('')
#comprimento, conta os elementos da tupla
print(len(lanche))

#ordem alfabética 
print(sorted(lanche))
print(lanche)

print(' ')
print(' ')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c) #juntar
print(d)
print(len(c)) #tamanho da tupla
# quantas vezes aparece o número 5
print(c.count(5)) # 2
# em 1ue posição está a posição 8
print(c.index(8)) # 4
print(d.index(8)) # 1
#deslocamento
print(d.index(5, 1))

#tuplas aceitam todo tipo de dados juntos
pessoa = ('Pedro', 25, 'M', 71.1)
#del(pessoa) apagar a tupla inteira
print(pessoa)