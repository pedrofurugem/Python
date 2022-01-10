#refazer
from datetime import date
atual = date.today().year
maior = 0 #usar contadores
menor = 0 # atribuir contatores
for c in range(1, 8):
    ano = int(input('digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - ano
    if  idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são de maiores'.format(maior))
print('{} pessoas são de menores'.format(menor))