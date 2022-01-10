sexo = ' ' #se for para string devo deixar a variável vázia
while sexo not in 'MmFf':
    sexo = str(input('digite seu sexo [M/F]: ')).upper()
    if sexo in 'Mm':
       print('sexo masculino registrado com sucesso')
    elif sexo in 'Ff': 
        print('sexo feminio registrado com sucesso')
    else: 
       print('invalido, só M ou F ')
print('FIM')