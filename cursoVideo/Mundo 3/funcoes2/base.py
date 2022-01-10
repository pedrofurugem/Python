#Interactive Help
#docstrings
#Argumentos opcionais
#Escopo de variáveis
#Retorno de resultados

#Interective Help
help(print)
print(input.__doc__)
     
#docstrings
def contador(i, f, p): #teclar aspas duplas 3 vezes para abrir a doc
    """
    -> faz uma contagem e mostra na tela
    :param i: primeiro valor
    :param f: ultimo valor
    :param p: passo
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
help(contador)

    #parametros opcionais
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')  
somar() # c = 0 quando aqui não é especificado um terceiro valor

#escopo de variáveis #compartilhando variáveis internas e globais
def funcao():
    n = 4
    print(f'N1 dentro vale {n}')
n = 2
funcao()
print(f'N1 global vale {n}')
  
  ### outro exemplo ###
def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}') # dividindo o mesmo valor de fora
    print(f'B dentro vale {b}') 
    print(f'C dentro vale {c}')
a = 5
teste(a)
print(f'A fora vale {a}') # dividindo o mesmo valor de dentro

    #retorno de resultados  return
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
    
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus calculos deram {r1}, {r2} e {r3}')


 ######## PRÀTICA ############
 #com fatorial
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')

#com par e impar
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

