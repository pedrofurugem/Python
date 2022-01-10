from datetime import date
atual = date.today().year 
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = atual - ano
categoria = atual - ano

print('O atleta nasceu em {}'.format(ano))
print('tem {} anos'.format(idade))
if categoria <= 9: 
    print('categoria: MIRIM')
elif categoria <= 14: 
    print('categoria: INFANTIL')
elif categoria <= 19:
    print('categoria: JUNIOR')
elif categoria <= 25:
    print('categoria: SENIOR')
else: 
    print('categoria: MASTER')