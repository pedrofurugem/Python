# notas 1, 10, 20 e 50
'''print(' $ ' * 15)
print('_________BEM VINDO ao caixa eletronico________')
print(' $ ' * 15)
cont1 = 0
cont10 = 0
cont20 = 0
cont50 = 0
while True:
    valor = int(input('Quanto você quer sacar: R$ '))
    if valor % 1 == 0:
       cont1 += 1
    if valor % 10 == 0:
       cont10 += 1
    if valor % 20 == 0:
       cont20 += 1
    if valor % 50 == 0:
       cont50 += 1
    break
print(f'emitidas {cont1} notas de 1')
print(f'emitidas {cont10} notas de 10')
print(f'emitidas {cont20} notas de 20')
print(f'emitidas {cont50} notas de 50')'''

print(' $ ' * 15)
print('_________BEM_VINDO_AO_BANCO________')
print(' $ ' * 15)
valor = int(input('Quanto você quer sacar? R$ '))
montante = valor
cedula = 50
totalced = 0
while True:
    if montante >= cedula:  #quantas vezes consigo extrair 50 do total
       montante -= cedula
       totalced += 1
    else:
        if totalced > 0:
            print(f' emitidas {totalced} cedulas de R${cedula}')
        if cedula == 50:
           cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total = 0
        if montante == 0: 
            break
print('Obrigado, volte sempre!')