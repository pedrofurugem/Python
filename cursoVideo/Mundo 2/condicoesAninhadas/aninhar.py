nome = str(input('qual é o seu nome? '))

if nome == 'Pedro': 
    print('nome bonito!')

elif nome == 'Gustavo' or nome == 'Maria' or nome == 'Paulo':
    print('seu nome é popular no Brasil')

elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome femino')

else: 
    print('seu nome é normal')
print('bom dia, {}'.format(nome))