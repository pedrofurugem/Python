#Exercício Python 106: Faça um mini-sistema que utilize 
# o Interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', 
# o programa se encerrará. 
# Importante: use cores.
from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
    ); #cores em uma lista

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='') #cor do manual será branco
    help(com) #comando de ajuda
    print(c[0], end='') #
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='') #c na posição [cor]
    print('~' * tam) #~ do tamanho da mesagem
    print(f'  {msg}')
    print('~' * tam) #~ do tamanho da mesagem
    print(c[0], end='') #pra ele limpar as cores
    sleep(1)

#programa princípal   
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2) # titulo aparecerá em verde \033[0;30;42m'
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando) #função ajuda com a variável comando dentro
titulo('ATÉ LOGO!', 1) # até logo aparecerá em vermelho - \033[0;30;41m