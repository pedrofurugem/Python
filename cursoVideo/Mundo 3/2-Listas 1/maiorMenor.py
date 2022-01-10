lista = []
maior = menor = 0
for c in range(0, 5): #nunca começar do 1
    lista.append(int(input(f'digite um valor na posição {c}: ')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] > maior:
           maior = lista[c]
        elif lista[c] < menor:
           menor = lista[c]
print(f'você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
