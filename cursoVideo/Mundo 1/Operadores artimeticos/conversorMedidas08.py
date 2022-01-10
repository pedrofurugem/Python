#Escreva um programaque leia um valor em metros e exiba convertido em
#centimetros e milimetros

n = float(input('digite um valor em metros: '))

centimetro = n * 100
milimetro =  centimetro * 10
kilometro =  n / 1000
print(n , 'metros') # pra fazer sem casa decimal é :.0f
print('o valor {:.2f} convertido para centimetro é: {:.0f} cm'.format(n, centimetro))
print('o valor {:.2f} convertido para milimetro é: {:.0f} mm'.format(n, milimetro))
print('o valor {} convertido para kilometro é: {} km'.format(n, kilometro))