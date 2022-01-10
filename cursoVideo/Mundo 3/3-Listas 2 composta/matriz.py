'''matriz = []
pos0 = []
pos1 = []
pos2= []
print('Vamos preencher a matriz: ')
for c in range(0, 1):
      pos0.append(int(input('Digite o valor para [0, 0]: ')))
      pos0.append(int(input('Digite o valor para [0, 1]: ')))
      pos0.append(int(input('Digite o valor para [0, 2]: ')))
      matriz.append(pos0[:])
      pos0.clear()
for c in range(0, 1):
      pos1.append(int(input('Digite o valor para [1, 0]: ')))
      pos1.append(int(input('Digite o valor para [1, 1]: ')))
      pos1.append(int(input('Digite o valor para [1, 2]: ')))
      matriz.append(pos1[:])
      pos1.clear()
for c in range(0, 1):
      pos2.append(int(input('Digite o valor para [2, 0]: ')))
      pos2.append(int(input('Digite o valor para [2, 1]: ')))
      pos2.append(int(input('Digite o valor para [2, 2]: ')))
      matriz.append(pos2[:])
      pos2.clear()
print('-=' *30)
print(f'[{matriz[0][0] :^5}] [{matriz[0][1] :^5}] [{matriz[1][1] :^5}]')
print(f'[{matriz[1][0] :^5}] [{matriz[1][1] :^5}] [{matriz[1][2] :^5}]')
print(f'[{matriz[2][0] :^5}] [{matriz[2][1] :^5}] [{matriz[2][2] :^5}]')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
      for c in range(0, 3):
         matriz[l][c] = int(input(f'digite o valor para a posição {[l]}{[c]}: '))
for l in range(0, 3):
   for c in range(0, 3):  
      print(f'[{matriz[l][c]:^5}]', end='') #formatação antes do colchete
   print() #quebra a linha