from datetime import date
atual = date.today().year
ano = int(input('digite o ano do nascimento do jovem: '))
print('nasceu em {}'.format(ano))
idade = atual - ano
print('você tem {} anos de idade'.format(idade))
cont = ano + 18
alistamento = atual - ano
passou = atual - cont
falta = cont - atual
 

if alistamento == 18: 
    print('hora de se alistar')
elif alistamento > 18: 
    print('ja passou o tempo ha {} anos'.format(passou))
elif alistamento < 18:
    print('ainda vai se alistar daqui {} anos'.format(falta))