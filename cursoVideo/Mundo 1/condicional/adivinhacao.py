#pensar em numero de 0 a 5
from random import randint
from time import sleep
computador = randint(0, 5) #início limite , faz o computador pensar
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:       
    print("Parabéns você sorteou o numero certo")
else:
     print("Infelizmente você não acertou")