'''frase = str(input('Digite uma frase e veja se ela é um palindromo: ')).strip().upper()
palavras = frase.split() #separar
junto = ''.join(palavras) #juntar
inverso = junto[::-1] #inverter
print(junto)
print(inverso)
if inverso == junto: #comparar
    print('é palindromo')
else:
    print('não é palindromo')'''
    
frase = str(input('Digite uma frase e veja se ela é um palindromo: ')).strip().upper()
print(frase)
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1): 
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print('é palindromo')
else: 
    print('não é um palindromo')
