print('*-' *20)
print('CAMPEONATO BRASILEIRO 2017')
print('*-' *20)
classificacao = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 
                 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico-MG', 'Botafogo',
                 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
                 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico-GO')

print('LIBERTADORES')
libertadores = classificacao[0:5]
print(f'Os 5 classificados para a libertadores são {libertadores}')

print('REBAIXAMENTO')
rebaixamento = classificacao[16:] # ou [-4:]
print(f'Os 4 ultimos colocados e rebaixados à serie-B 2018 foram {rebaixamento}')

print('ORDEM ALFABÉTICA')
print(sorted(classificacao))

posChape = classificacao.index('Chapecoense')+1
print(f'A Chapecoense esta na {posChape}º posicao')
