lista = []
cont = 0
while True: 
    n = int(input('digite um número: '))
    lista.append(n)
    cont += 1
    opcao = str(input('deseja continuar?[S/N]: ')).upper().strip()[0]
    if opcao not in 'Ss':
       break
print(f'{sorted(lista)}')
print(f'foram digitados {cont} números')
lista.sort(reverse=True)
print(f'ordem decrescente = {lista}')
if 5 in lista:
    print(f'o numero 5 foi digitado na lista')
else:
    print('o número 5 não foi digitado')
