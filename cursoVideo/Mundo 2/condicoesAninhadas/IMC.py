#fórmula: IMC = peso/ (altura x altura)
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
print('peso = {:.1f}Kg'.format(peso))
print('altura = {:.2f}'.format(altura))
IMC = peso / (altura * altura)
print('seu IMC é de {:.2f}'.format(IMC))

if IMC < 18.5: 
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC < 25: 
    print('Peso ideal')
elif IMC >= 25 and IMC < 30: 
    print('Sobrepeso')
elif IMC >= 30 and IMC < 40: 
    print('Sobrepeso')
else: 
    print('Obesidade morbida, TA GORDÃO HEIN')