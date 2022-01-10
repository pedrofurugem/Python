aluno = dict()
aluno['nome'] = str(input('digite o nome no aluno: '))
aluno['media'] = float(input('digite a media: '))
print(f'o nome do aluno é {aluno["nome"]}')
print(f'Sua media foi de {aluno["media"]}')
if aluno['media'] >= 7.00: aluno['situação'] = 'Aprovado'
elif aluno['media'] > 5.00 or aluno['media'] < 7.00: aluno['situação'] = 'Recuperação'
else: aluno['situação'] = 'Reprovado'

#para cada chave um valor
for k, v in aluno.items():
    print(f'{k} é igual a {v}')