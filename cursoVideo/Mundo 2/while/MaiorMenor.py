# o n teria que fazer arte do loop
# um detalhe, deve-se fazer a soma contagem e media antes da mensagem do loop
media = soma = cont = maior = menor = 0
opcao = 'Ss'
while opcao in 'Ss':
    n = int(input('digite um número: '))
    soma += n
    cont += 1
    opcao = str(input('dejesa continuar[S/N]: ')).upper().strip()[0]
    media = soma / cont
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('A soma de tudo é {}'.format(soma))
print('media = {}'.format(media))
print('O maior foi {}'.format(maior))
print('O menor foi {}'.format(menor))
print('FIM')