#meu jeito
#import random
#from time import sleep
#print('escolha um desses 4 alunos')
#lista = ('Ana Maria Bia Carlos Dudu').split()
#sleep(2)
#alunos = random.choice(lista)
#print('O aluno(a) sorteado a apagar o quadro foi: {}'.format(alunos))

#guanabara
import random
#from time import sleep
n1 =  str(input('Primeiro aluno: '))
n2 =  str(input('segundo aluno: '))
n3 =  str(input('Terceiro aluno: '))
n4 =  str(input('quarto aluno: '))
lista = [n1, n2, n3, n4] 
#sleep(2)
print('O aluno(a) sorteado a apagar o quadro foi: {}'.format(random.choice(lista)))
