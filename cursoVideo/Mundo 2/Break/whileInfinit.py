#feito com a gambiarra
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s - 999))

# Feito com a técnica certa comando break
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')


#Outos exemplos com FStrings
nome = 'Zé Pinto'
idade = 33
salario = 987.35
# ^centro <esquerda >direita
print(f'seu nome é {nome:-^20} ele tem {idade} anos e ganha R${salario}') # PYTHON 3.6 + ultima versão
print('Seu nome é {} ele tem {} anos'.format(nome, idade)) # PYTHON 3
print('Seu nome é %s ele tem %d anos.' % (nome, idade)) #PYTHON @