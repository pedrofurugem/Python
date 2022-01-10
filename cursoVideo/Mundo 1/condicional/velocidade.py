vel = float(input('Digite a velocidade Km do carro '))

print('{:.2f} km'.format(vel))
limite = vel - 80
multa = limite * 7.00

if vel > 80:
    print('Pra seu azar você foi multado')
    print('O valor da multa é de R$ {:.2f}'.format(multa))
else: 
    print('Ta beleza')