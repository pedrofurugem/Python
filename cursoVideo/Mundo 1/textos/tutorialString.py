#indica o que tem na posição 4, lembrando que sempre começa do 0
frase = 'Curso em video Python'
print(frase[4]) # o

#fatiar de 3 a 13
frase = 'Curso em video Python'
print(frase[3:13]) #so em vide

#da posição 13 para frente
frase = 'Curso em video Python'
print(frase[13:])#o Python

# do 1 ao 15 pulando duas casas
frase = 'Curso em video Python'
print(frase[1:15:2])#us mvdo

#salto de duas em duas letras
frase = 'Curso em video Python'
print(frase[::2])#Croe ie yhn

#para textos grandes coloca-se ''' 3 aspas
print('''Minha vida esta uma merda por completo''')

#contando quantas letras especificas "o"
frase = 'Curso em video Python'
print(frase.count('o'))

#minusculo
frase = 'Curso em video Python'
print(frase.lower())

#maiusculo
frase = 'Curso em video Python'
print(frase.upper())

#combinando elementos
#quantidade de O em maiusculo
frase = 'Curso em video Python'
print(frase.upper().count('O'))

#contando a quantidade total de caracteres
frase = 'Curso em video Python'
print(len(frase))

#remove os espaços
frase = '  Curso em video Python  '
print(len(frase.strip()))

#trocando palavras com replace
frase = 'Curso em video Python'
print(frase.replace('Python', 'Android'))#Curso em video Android

#uma string é imutavel, se eu quiser salvar com uma palavra nova
#frase = 'Curso em video Python'
#frase = (frase.replace('Python', 'Android'))
#print = frase #Curso em video Android  AQUI ALTEROU A STRING

#encontrando palavra especifica
frase = 'Curso em video Python'
print(frase.find('video'))

#buscar video em minusculo 
frase = 'Curso em video Python'
print(frase.lower().find('video'))

#dividindo as palavras com split
frase = 'Curso em video Python'
print(frase.split())

#
frase = 'Curso em video Python'
dividido = frase.split()
print(dividido[0]) #['Curso', 'em', 'video', 'Python']

#pegar o dividido 2 e a posição 3
frase = 'Curso em video Python'
dividido = frase.split()
print(dividido[2][3]) #video posição 2 e e na posição 3

