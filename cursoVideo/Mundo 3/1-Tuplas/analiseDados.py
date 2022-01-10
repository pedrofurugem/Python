cont = 0
n = (int(input('Digite o primeiro numero: ')),
    int(input('Digite o segundo numero: ')),   
    int(input('Digite o segundo numero: ')),  
    int(input('Digite o segundo numero: ')))
print(f'Você digitou os valores {n}')
print(f'o valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
   print(f'o valor 3 apareceu pela primeira vez na posição {n.index(3)+1}')
else: print('não tem valor 3')
for c in n:
    if c % 2 == 0:
       cont += 1
print(f'Apareceram {cont} numeros pares')
#nunca n % 2 == 0

