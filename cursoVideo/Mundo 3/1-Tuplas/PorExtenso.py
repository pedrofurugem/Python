#meu jeito
lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezete', 'dezoito',
'dezenove', 'vinte')

#CONTINUAR
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if  0 <= n <= 20: #a forma correta
        break
    print('Tente novamente. ', end=' ')
print(f'Você digitou o número {lista[n]}')