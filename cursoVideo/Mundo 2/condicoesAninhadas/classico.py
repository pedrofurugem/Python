n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

media = (n1 + n2) / 2
print('a media foi de {}'.format(media))
if media < 5.0:
    print('REPROVADO')
elif media > 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')