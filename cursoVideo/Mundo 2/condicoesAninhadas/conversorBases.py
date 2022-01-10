#24 = 2x101 + 4x100 = 2x10 + 4x1 = 24.
#Se o número fosse 124, seria: 1x102 + 2x101 + 4x100 = 1x100 + 2x10 + 4x1 = 124.
#3124? 3x103 + 1x102 + 2x101 + 4x100 = 3x1000 + 1x100 + 2x10 + 4x1 = 3124.

#como vou dividir os algarismos?
# conversor de bases, binario, octal e hexadecimal
n = int(input('digite um numero: '))
print(n)
base = int(input('Selecione uma base de convserão: '))
print('''
1- BINÁRIO  
2- OCTAL
3 - HEXADECIMAL
''')

if base == 1: 
   print('{} convertido para binario é igual a{}'.format(n, bin(n) [2:])) #fatiamento
elif base == 2: 
   print('{} convertido para octal é igual {}'.format(n, oct(n) [2:])) #fatiamento
elif base == 3: 
   print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n) [2:])) #fatiamento
else: 
    print('digite uma opção valida')