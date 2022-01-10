from time import sleep
def contador(i, f, p):
    print(f'contagem de {i} em {f} de {p} em {p}')
    sleep(1.5)
    
    #Em caso de número negativo
    if p < 0: #resolvendo o problema com negativos
        p *= -1
    if p == 0: #e se caso o passo for igual a zero
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True) #lembrar do flus
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('agora, é sua vez de contar')
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
contador(i, f, p)

'''
deu certo com for, MAS não conta o ultimo número 
if i < f:
        for c in range(i, f, p):
            sleep(0.5)
            print(f'{c}', end =' ', flush=True)
        print('FIM')
    elif i > f:
        for c in range(i, f, -p):
            sleep(0.5)
            print(f'{c}', end =' ', flush=True)
        print('FIM')
'''