d = float(input('Qual a distancia da viagem? '))

print('{}Km'.format(d))
if d <= 200:  
    preço = d * 0.50
    print('O preço da passagem é de R${:.2f}'.format(preço))
else: 
    preço = d * 0.45
    print('O preço da passagem é de R${:.2f}'.format(preço))


#forma simplificada
# coloque 0 para anpreco = d * 0.50 id d <= 200 else d * 0.45