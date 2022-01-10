# programas dentro de outros programas, tive problemas com o loop infinito
# refeito
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
opcao = 0
while opcao < 5:
    print('[1]somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]novos números')
    print('[5]sair do programa')
    opcao = int(input('digite uma das opções acima de 1 a 5: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    if opcao == 2:
        mult = n1 * n2
        print('{} * {} = {}'.format(n1, n2, mult))
    if opcao == 3:
        if n1 > n2:
            print('{} é o maior'.format(n1))
        elif n2 > n1:
            print('{} é o maior'.format(n2))
        else:
            print('  valores iguais')
    if opcao == 4:
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
    if opcao == 5:
        print('finalizando...')
    else: 
        print('opção invalida')
print('FIM DO PROGRAMA')