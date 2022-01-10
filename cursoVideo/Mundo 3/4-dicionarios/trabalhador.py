#fiz sozinho
cadastro = dict()
from datetime import date
atual = date.today().year
while True:
    cadastro['nome'] = str(input('nome: '))
    nascimento = int(input('ano de nascimento: '))
    cadastro['idade'] = atual - nascimento
    cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
    if cadastro['CTPS'] == 0:
        break
    else:
        cadastro['ano de contratação'] = int(input('ano de contratação: '))
        cadastro['salario'] = float(input('salario R$'))
        dif = atual - cadastro['ano de contratação'] #ano atual menos ano de contratação
        cadastro['aposentadoria'] = (cadastro['idade'] - dif) + 35 #aposentaoria = ano de cadastro - a diferença + 35
        break
print('-=' *30)
for i, v in cadastro.items():
    print(f' - {i} tem o valor {v}')