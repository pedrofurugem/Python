from datetime import date

ano = int(input("Digite um ano que você queira analisar. Coloque 0 para nalisar o ano atual "))
if ano == 0:
    ano == date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print('{} é um ano bisexto'.format(ano))
else: 
    print('{} não é um ano bisexto'.format(ano))
