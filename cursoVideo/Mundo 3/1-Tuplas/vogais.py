#tentar mais uma vez
palavra = ('APRENDER', 'PROGRAMAR', 'LIGUAGEM', 'PYTHON', 'CURSO',
         'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
         'PROGRAMADOR', 'FUTURO')
for c in palavra:
    print(f'\nna palavra {c} temos: ', end=' ')
    for letra in c:
        if letra in 'AEIOU':
            print(letra.upper(), end=' ')