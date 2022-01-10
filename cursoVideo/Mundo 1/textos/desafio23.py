#faça um programa que leia um numero de 0 a 99 
#e mostre na tela cada um dos digitos separados
#"separar digitos de um numero"
n = int(input('digite um numero de 0 a 9999: '))
u = n // 1 % 10 #// pra não pegar resto
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('analisando o numero {}'.format(n))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))




#trabalhando com string
#num = int(input('digite um numero de 0 a 9999: '))
#n = str(num)
#print('analisando o numero {}'.format(num))
#print('unidade: {}'.format(n[3]))
#print('dezena: {}'.format(n[2]))
#print('centena: {}'.format(n[1]))
#print('milhar: {}'.format(n[0]))