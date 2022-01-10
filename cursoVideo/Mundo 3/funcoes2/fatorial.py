def fatorial(num, show=False): #não esquecer das docstrings
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número
    """
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='') 
            if c > 1:
                print(' x ', end='')
            else: 
                print(' = ', end='')
        fat *= c 
    return fat
#Programa princípal
n = int(input('digite um numero para calcular seu fatorial: '))
print(fatorial(n, show=True))
help(fatorial)