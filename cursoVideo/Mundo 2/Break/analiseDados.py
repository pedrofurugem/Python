contIdade = 0
contHomens = 0
contMulheres = 0
while True:
    idade = int(input('digite sua idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('seu sexo[M/F]: ')).upper().strip()[0]
    if idade > 18:
       contIdade += 1
    if sexo in 'Mm':
       contHomens += 1
    if sexo in 'Ff' and idade < 20:
       contMulheres += 1
    continua = ' '
    while continua not in 'SN': 
       continua = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print(f'{contIdade} pessoas tem mais de 18 anos')
print(f'{contHomens} homens cadastraram')
print(f'{contMulheres} muheres tem menos de 20 anos')