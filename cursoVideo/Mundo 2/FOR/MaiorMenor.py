#refazer
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('digite o peso da {}° pessoa: '.format(c)))
    if c == 1: #lendo o peso da primeira pessoa
        maior = peso 
        menor = peso
    #posso fazer com elif também
    elif peso > maior: # o maior peso passa a ser o proximo da lista
            maior = peso
    elif peso < menor: # o menor peso passa a ser o proximo da lista
            menor = peso
print('o maior peso lido foi de {}kg'.format(maior))
print ('o menor peso lido foi de {}kg'.format(menor))   