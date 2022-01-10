#Faça um programa que lei o nome completo de uma pessoa
#mostrando em seguida o primeiro eo ultimo nome separadamente
#Ex: Pedro Roberto Furuguem
#primeiro: Pedro
#ultimo: Furuguem

nome = str(input("Digite seu nome completo: ")).strip()
primeiro = nome.split()
ultimo = nome.split()
print('Muito prazer em te conhecer!')
print('seu nome completo é: {}'.format(nome))
print('seu primeiro nome é: {}'.format(primeiro[0]))
print('seu ultimo nome é: {}'.format(ultimo[len(ultimo)-1])) #para procurar a ultmia palavra em uma split
