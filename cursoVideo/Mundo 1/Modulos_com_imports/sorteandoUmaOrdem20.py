import random
n1 =  str(input('Primeiro aluno: '))
n2 =  str(input('segundo aluno: '))
n3 =  str(input('Terceiro aluno: '))
n4 =  str(input('quarto aluno: '))
lista = [n1, n2, n3, n4] 
#sequencia = random.sample(lista, len(lista)) # embaralhar uma sequencia
random.shuffle(lista)
print('A sequencia de apresentação de trabalhos foi a seguinte: {}'.format(lista))


#.sample(x, k=len(x))