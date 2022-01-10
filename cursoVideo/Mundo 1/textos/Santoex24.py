#Fazer um programa que leia uma cidade e diga se começa com Santo
cidade = str(input("digite o nome de uma cidade: ")).strip() #strip para eliminar vazios
print(cidade[:5].upper() == 'SANTO')

