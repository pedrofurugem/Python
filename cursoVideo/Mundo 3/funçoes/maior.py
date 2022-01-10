def maior(* n, cont=0, maior=0):
    print('-=' * 30)
    print('Analisando valores passados...')
    for c in n:
        cont += 1
        print(c, end=' ')
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
    print(f'Ao todo foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')
   

#programa princípal 
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
