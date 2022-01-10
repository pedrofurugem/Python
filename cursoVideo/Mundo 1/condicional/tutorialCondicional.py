#condicional simples
nome = str(input('Qual é seu nome? '))
if nome == "Pedro": 
   print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

#condicional composta 
nome = str(input('Qual é seu nome? '))
if nome == "Pedro": 
    print('Que nome lindo você tem!')
else: 
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

#programa classico das notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 +n2) / 2
print('A sua media foi {:.1f}'.format(m))
if m >=6:  
   print('Sua media foi boa!, PARABÉNS')  
else:  
  print('Sua média foi rum!, ESTUDE MAIS!')

#if simplificado
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 +n2) / 2
print('A sua media foi {:.1f}'.format(m))
print('PARABÉNS' if m>=6 else 'ESTUDE MAIS!')