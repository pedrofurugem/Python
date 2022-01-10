# break não pode terminar em If
# o break só deve funcionar somente dentro de um While True
from random import randint
print('^^' * 30)
print('Sou seu computador vamos tirar no PAR OU IMPAR?')
print('^^' * 30)
v = 0
while True:
    jogador = int(input('jogue um número de 1 a 10: '))
    computador = randint(1, 10)
    resultado = jogador + computador
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('escolha P (par) ou I (impar) [P/I]: ')).upper().strip()[0] 
    print(f'computador escolheu {computador}')   
    if  escolha == 'P':
        if resultado % 2 == 0:  
            print('Você venceu')
            v += 1
        else:
            print('Perdeu!')
            break
    elif escolha == 'I':
        if resultado % 2 == 1:  
            print('Você venceu')
            v += 1
        else:
            print('Perdeu!')
            break
    print('Vamos jogar novamente...')
print('Jogo de tirar para ou impar encerrado')
if v > 1:
   print(f'você venceu {v} vezes')
elif v == 0: 
    print('Nenhuma vitória')
else:
    print(f'você venceu apenas {v} vez')
