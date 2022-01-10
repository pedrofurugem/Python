import random
from time import sleep
print('vamos tirar no JOKENPÔ')
print('FAÇA SUA ESCOLHA')
print('pedra')
print('papel')
print('tesoura')
jogada = str(input('Qual a sua jogada? '))
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)


sleep(1)
print('JÓ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('')
print(computador)
print('')
if jogada == 'pedra' and computador == 'papel':
    print('papel embrulha pedra, você perdeu')

elif jogada == 'papel' and computador == 'pedra':
    print('papel embrulha pedra, você venceu')

elif jogada == 'pedra' and computador == 'tesoura':
    print('pedra quebra tesoura, você venceu')

elif jogada == 'tesoura' and computador == 'pedra':
    print('pedra quebra tesoura, você perdeu')
    
elif jogada == 'papel' and computador == 'tesoura':
    print('tesoura corta papel, você perdeu')

elif jogada == 'tesoura' and computador == 'papel':
    print('tesoura corta papel, você venceu')

elif jogada == computador:
    print('EMPATE')

else:
    print('jogue entre pedra, papel ou tesoura')