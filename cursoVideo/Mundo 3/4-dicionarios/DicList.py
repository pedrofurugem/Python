dados = dict()
lista = list()
cont = soma = media = 0
while True:
    dados['nome'] = str(input('nome: ')).strip()
    cont += 1
    while True:
        dados['sexo'] = str(input('sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Só digite M ou F')
    dados['idade'] = int(input('idade: '))
    lista.append(dados.copy())
    soma += dados['idade']
    media = soma / cont
    while True:
        opcao = str(input('quer continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('Só digite S ou N')
    if opcao in 'N':
        break
lista.append(dados.copy())
#a) total de pessoas
print('-=' *30)
print(f'Ao todo cadastraram {cont} pessoas')
#b) media de idade
print('-=' *30)
print(f'A media de idade é {media:.2f}')
#c) lista de mulheres
print('-=' *30)
print(f'As mulheres cadastradas são: ', end=' ')
for f in lista:
    if f['sexo'] in 'F':
       print(f'{f["nome"]}')
#d) idade acima da media
print('-=' *30)
print('As pessoas com idade a cima da media são: ')
for m in lista:
    if m['idade'] >= media:
       print(f'{m["nome"]}')
print('FIM')

