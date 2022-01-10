#melhoramento do desafio 28
'''from random import randint
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
     print("Infelizmente você não acertou")'''



#fazer novamente
from random import randint
from time import sleep
print('Ola sou seu computador! será que você é capaz de adivinhar qual numero escolhi de 0 a 10?')
computador = randint(1, 10)
cont = 0
palpite = 0
while computador != palpite:
      palpite = int(input('dê seu palpite de 0 a 10: '))
      cont += 1
      if palpite == computador:
        sleep(1)
        print('Parabéns você acertou com {} palpite(s)'.format(cont))
      elif palpite > 10 or palpite == 0:
        print('O palpite só vale de 0 a 10')
      elif palpite > computador: 
          print('menos tente novamente')
      elif palpite < computador:
          print('mais, tente novamente')
print('FIM')