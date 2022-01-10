def aumentar(preco=0, taxa=0, formato=False):
    '''
    -> Programa para formatação de moedas
    :param  preco: o preço que você quer reajustar
    :param  taxa: qual a porcentagem do aumento
    :param  formato: quer a saída formatada ou não?
    Returns: valor ajustado com o seu formato
    '''
    r = preco + (preco * taxa / 100)
    return r if formato is False else moeda(r)  # retorna a formatação


def diminuir(preco=0, taxa=0, formato=False):
    r = preco - (preco * taxa / 100)
    return r if formato is False else moeda(r)


def dobro(preco=0, formato=False):
    r = preco * 2
    return r if formato is False else moeda(r)


def metade(preco=0, formato=False):
    r = preco / 2
    return r if formato is False else moeda(r)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco, aum=20, dim=12):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')  # tabulação
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aum}% de aumento: \t{aumentar(preco, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(preco, dim, True)}')
    print('-' * 30)