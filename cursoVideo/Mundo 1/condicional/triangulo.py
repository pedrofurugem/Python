a = int(input('valor da primeira reta: '))
b = int(input('valor da segunda reta: '))
c = int(input('valor da terceira reta: '))

#a soma de dois lados é sempre menor que o terceiro lado.
print('-=' *20)
print('Analisando um triangulo')
print('-=' *20)

if a < b+c and b < a+c and c < a+b:
    print('FORMA UM TRIANGULO')
else:  
    print('NÃO FORMA UM TRIANGULO')