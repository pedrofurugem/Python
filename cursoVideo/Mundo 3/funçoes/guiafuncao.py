#rever a aula de função
def lin ():
    print('-' *30)
#programa princípal

lin()
print('   CURSO EM VIDEO  ')
print('   APRENDA PYTHON  ')
print('   PEDRO ROBERTO   ')
lin()

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)
titulo(' CURSO EM VIDEO ')
titulo(' PYTHON ')
titulo('oi') 

def soma(a, b):
   s = a + b 
   print(s)
   
#promgrama principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

def soma(a, b):
    print('A={a} e B ={b}')
    s = a + b
    print(f'A soma A + B = {s}')
soma(b=4, a=5)
soma(7, 2)


def contador(* n): 
    print(n)
    
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def contador(* n):
    for valor in n:
        print(f'{valor}', end=' ')
    print('FIM')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def contador(* n): #vou receber parametros
    tam = len(n)
    print(f'Recebi os valores {n} e são ao todo {tam} números')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

##funções com listas
#ficar atento com isso
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def soma(* valores):  #desempacontamento
    s = 0 
    for n in valores: 
        s += n
    print(f'Somando os valores {valores} temos {s}')   
soma(5, 2)
soma(2, 9, 4)

def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

contador(2, 10, 2)

def mensagem(msg):
    print('------')
    print(msg)
    print('-------')
mensagem('SISTEMA DE ALUNOS')
# a frase sistema de alunos vai para msg dentro da função
 #outro exemplo
def titulo(txt):
    print('-' *30)
    print(txt)
    print('-' *30)
titulo(' CURSO EM VIDEO ')
titulo('SISTEMA DE ALUNOS')
titulo('porraaaaaaaaaaaaaa')


def contador(* n):#desepacotador
    print('')
contador(5, 7, 3, 1, 4)
contador(8, 7, 4)