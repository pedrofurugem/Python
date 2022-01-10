s = 0 
for n in range(1, 6+1): 
    n = int(input('digite {}° valor: '.format(n)))
    if n % 2 == 0:
        s += n
print('A soma dos pares é igual a {}'.format(s))