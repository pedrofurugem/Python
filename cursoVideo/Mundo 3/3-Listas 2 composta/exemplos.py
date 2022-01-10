#lista dentro de outra lista 
dados = list()
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
pessoas.append(dados[:])
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

#prática
#compartilhando lista com outra lista
teste = list()
teste.append('Pedro')
teste.append(25)
galera = list()
#aqui criei uma ligação entre as duas estruturas
galera.append(teste[:]) #copia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #copia
print(galera)

#outro exemplo
galera = [['Maria', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1]) #posição 2 idade do Joaquim #pega o dado da posição 2 e o item da posição 1 do dado 2
for p in galera:
    #print(p[0]) #só os nomes
    print(f'{p[0]} tem {p[1]} anos de idade.')
     
galera = list()
dado = list() #temporario
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #sem [:] -> [[], [], [], [], []]
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é de menor')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores')