aluno = list()
while True: 
    nome = str(input('digite o nome do aluno: '))
    n1 = float(input('digite a primeira nota: '))
    n2 = float(input('digite a segunda nota: '))
    media = (n1 + n2) / 2
    aluno.append([nome, [n1, n2], media])
    while True:
        opcao = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('ERRO! digite S OU N')
    if opcao in 'N':
        break
print(aluno)
#fazer aninhamento e pegar um aluno específico 
print('-=' *30)
print(f'{"No":<4} {"Nome":<10} {"Media":>8}')
print('-' *40)
for i, a in enumerate(aluno):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}') #tentar especifícar as areas para ele não buscar o ultimo
print()
#Fazendo a busca
while True:
    busca = int(input('digite o codigo do aluno na tabela ou [999] para sair: '))
    if busca == 999:
        print('FINALIZANDO')
        break
    if busca <= len(aluno) -1: 
        print(f' Notas do aluno {aluno[busca][0]} são: {aluno[busca][1]}')