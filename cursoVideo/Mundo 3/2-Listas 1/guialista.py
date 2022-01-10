# tupla = ('burgue', 'refri', 'batata')
#n = (2, 5, 9, 1) #tupla
#n[2] = 3  tuplas são imútaveis
#print(n)
#LISTAS

n = [2, 5, 9, 1] 
n[2] = 3  #trocando elemento
n.append(7)#inserindo novo elemento
n.sort() #colocando em ordem
n.sort(reverse=True)#invertendo ordem
n.insert(2, 0) # adiciona um 0 na posição 2
n.pop() #elimina o ultimo elemento se mandar vazio
n.pop(2) #removendo um elemento
n.insert(2, 2)
n.remove(2) #remove o primeiro elemento 2
if 4 in n:
    n.remove(4)
else:
    print('Não encontrei o número 4')
print(n)
print(f'Essa lista tem {len(n)} elementos')

valores = []
#valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

#for v in valores: 
#    print(f'{v}...', end='')
#[5, 9, 4]
#5...9...4...

for c, v in enumerate(valores): 
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da lista')
 #   [5, 9, 4]
#Na posição 0 encontrei o valor 5...
#Na posição 1 encontrei o valor 9...
#Na posição 2 encontrei o valor 4...


valores = list()
for cont in range(0, 5): 
    valores.append(int(input('Digite uma valor: ')))
print('FIM')

a = [2, 3, 4, 7]
b = a[:] #neste caso b rece fatiamento de a criando sua propria lista
b = a #aontece neste caso
b[2] = 8 #se uma lista "é igual" a outra o python cria uma ligação entre elas
print(f'Lista A: {a}')
print(f'Lista B: {b}')