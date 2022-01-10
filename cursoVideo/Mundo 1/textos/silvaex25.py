# Fazer um programa que leia um nome e procure SILVA no nome
#meu jeito
#nome = str(input("digitie seu nome: ")).strip()
#print(nome[6:].upper() == 'SILVA')

#com operador in, se tem a palavra
nome = str(input('digite seu nome: ')).strip()
print('Seu nome possui "SILVA"? {}'.format('SILVA' in nome.upper().split()))

#nome = str(input('digite seu nome: ')).strip()
#print('Seu nome possui "SILVA"? {}'.format('silva' in nome.lower()))
