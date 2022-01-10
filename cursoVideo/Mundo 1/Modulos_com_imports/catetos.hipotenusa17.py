#meu jeito
#from math import sqrt

#print('calculando triangulo retangulo')
#co = float(input('digite o valor do cateto oposto: '))
#ca = float(input('digite o valor do cateto adjacente: '))

#h = (co * co) + (ca * ca)
#print('O valor da hipotenusa de {} e {} é igual a {}'.format(co, ca, sqrt(h)))

#importando o calculo da hipotenusa
from math import hypot
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))

hi = hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}'.format(hi))
