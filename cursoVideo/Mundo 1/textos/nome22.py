# contar o nome todo
#contar o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip() #tirar os espaços
print('seu nome em maiusculas é '.format(nome.upper()))
print('seu nome em minusculas é '.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' '))) # conta a quantidade menos os espaços em branco
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() # a split separa palavras
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))