#aqui só foi um exemplo
nome = 'Pedro Furuguem'
maiusculas = nome.upper()
minusculas = nome.lower()
total = len(nome) - nome.count(' ')
detalhe = nome.split()


print('seu nome em maiusculas é {}'.format(maiusculas))
print('seu nome em minusculas é {}'.format(minusculas))
print('seu nome tem ao todo {} letras'.format(total))
print('seu primeiro nome é {} e ele tem {} letras'.format(detalhe[0], len(detalhe[0])))