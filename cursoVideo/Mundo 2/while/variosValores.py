#consegui 80% deste exercício 
n = soma = cont = 0
while n != 999:
    n = int(input('digite um número: '))
    soma += n
    cont += 1
print('foram digitados {} numeros'.format(cont))
print('Soma = {}'.format(soma - 999))