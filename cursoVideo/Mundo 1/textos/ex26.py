#Faça um programa que leia a frase pelo teclado e mostre
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

#MEU jeito
#problema com as maiusculas
#problema de aparecer a posição 0
#1° tentativa
#frase = str(input('digite uma frase: ')).strip()
#print('a letra "a" aparece', frase.count('a'), 'vez(s)')
#print('na primeira vez na posicao', frase.find('a'))
#print('e na ultima vez na posicao', frase.rfind('a'))

#meu jeito
frase = str(input('digite uma frase: ')).upper().strip()
total = frase.count('A')
primeira = frase.find('A') + 1 # o +1 é para não contar a posição zero
ultima = frase.rfind('A') 
print('a letra "A" aparece {} vezes'.format(total))
print('na primeira {}° posicao'.format(primeira))
print('na ultima em {}° posicao'.format(ultima))


#Guanabara
frase = str(input('digite uma frase: ')).upper().strip()
print('a letra "A" aparece {} vezes'.format(frase.count('A')))
print('A primeira letra "A" apareceu na {}° posicao'.format(frase.find('A')+1))
print('A ultima letra "A" apareceu na {}° posicao'.format(frase.rfind('A')))