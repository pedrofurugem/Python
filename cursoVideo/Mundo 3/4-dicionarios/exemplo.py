#Dicionário {}
pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 25}
del pessoas['sexo'] #apagar um item no discionario
pessoas['nome'] = 'Roberto' #alterando um item no discionario
pessoas['peso'] = 71.1 #adicionando um elemento no discionario
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #a formatação só pode ser feita desta maneira
print(pessoas.keys()) #dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) #dict_values(['Pedro', 'M', 22])
print(pessoas.items()) #dict_items([('nome', 'Pedro'), ('sexo', 'M'), ('idade', 22)])

for k in pessoas.keys(): # nome
    print(k)
    
for v in pessoas.values(): # Pedro
    print(v) 
    
for k, v in pessoas.items(): #nome: Pedro
    print(f'{k} = {v}')
    
# Criar um dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
#uma forma de printar o dado
print(brasil[1]['sigla'])
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #metodo copy diferente do fatiamento
#for e in brasil:
    #for k, v in e.items(): #contador nos items
        #print(f'O campo {k} tem valor {v}')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
