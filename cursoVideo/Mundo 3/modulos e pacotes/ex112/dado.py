#fazer sozinho e rever validação de dados
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':#se é alpha numérico
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)
