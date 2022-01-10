def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[00;31mdigite um número inteiro válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[00;31musuário preferiu não digitar esse número \033[m')
            return 0
        else:
            return n
    
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[00;31mdigite um número float válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[00;31musuário preferiu não digitar esse número \033[m')
            break
        else:
            return n
    
#programa principal
i = leiaInt('digite um numero inteiro: ')
print(f'O valor digitado foi {i}')
f = leiaFloat('digite um numero de ponto flutuante: ')
print(f'O valor digitado foi {f}')



#print('\033[00;31mERRO! Digite um número válido. \033[m')

#TIPOS DE ERROS

#ValueError -> indicar que algo anormal aconteceu durante a execução do seu código
#TyeError ->  representa um erro de quando um valor não é do tipo esperado
#KeiboardInterrupt ->  quando não digita nada
