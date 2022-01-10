def leiaInt(msg):   
    valeu = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            valeu = True
        else:
            print('\033[00;31mERRO! Digite um número válido. \033[m')
        if valeu:
            break
    return valor
#programa principal
n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número: {n}')

#print('\033[00;31mERRO! Digite um número inteiro válido.\033[m') #\033 pra fechar