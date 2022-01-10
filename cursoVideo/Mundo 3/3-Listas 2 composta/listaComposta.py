# galera.append(dado[:])
lista = list()
pessoa = list()
cont = maior = menor = 0
while True:
    nome = str(input('digite o nome: '))
    pessoa.append(nome)
    peso = float(input('digite o peso: '))
    pessoa.append(peso)
    cont += 1
    if len(lista) == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('quer continuar? [S/N]: ')).upper().strip()[0]
    if opcao not in 'Ss':
        break
#a)
print(f'{cont} pessoas se cadastraram')

#b)pra mostrar o nome crio outro FOR
for p in lista:
    if p[1] == maior:
       print(f'[{p[0]}]')
print(f'O maior peso foi {maior}kg')

#c)mesma coisa aqui
for p in lista:
    if p[1] == menor:
      print(f'[{p[0]}]')
print(f'O menor peso foi {menor}kg')
