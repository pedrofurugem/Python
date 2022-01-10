matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma = maior = 0
for l in range(0, 3):
      for c in range(0, 3):
            matriz[l][c] = int(input(f'digite um valor na posição [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
      for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
            if matriz[l][c] % 2 == 0:
                  somapar += matriz[l][c]
      print()
 #refazer
#a) soma dos valores pares digitados
print(f'A soma dos valores pares digitados é {somapar}')

#b) soma dos valores da terceira coluna
#print(f'Soma dos valores da terceira coluna = {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
for l in range(0, 3):
      soma += matriz[l][2]
print(f'Soma dos valores da terceira coluna = {soma}')

#c) o maior valor da segunda linha
for c in range(0, 3):
      if c == 0:
           maior = matriz[1][c]
      else:
            if matriz[1][c] > maior:
                  maior = matriz[1][c]
            
print(f'O maior valor da segunda linha é {maior}') 
      