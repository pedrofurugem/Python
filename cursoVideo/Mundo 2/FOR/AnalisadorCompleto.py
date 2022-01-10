###Refazer
s = 0
maior = 0
nomeVelho = 0
menor20 = 0
for c in range(1, 5): 
    nome = str(input('qual o nome da {}° pessoa: '.format(c)))
    idade = int(input('qual a idade {}° pessoa: '.format(c)))
    sexo = str(input('sexo [M/F]: ')).upper()
    s += idade
    media = s / 4
    if c == 1 and sexo in 'Mn': 
        maior = idade 
        nomeVelho = nome
    if sexo in 'Mn' and idade > maior:
        maior = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        menor20 += 1
print('a media de idade é de {} anos'.format(media))
print('o homem mais velho tem {} anos e seu nome é {}'.format(maior, nomeVelho))
print('a todo são {}  mulherer(s) com menos de 20 anos'.format(menor20))