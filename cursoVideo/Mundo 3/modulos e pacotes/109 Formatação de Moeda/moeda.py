def aumentar(preco=0, taxa=0, formato=False):
    """
    Programa para formatação de moedas
    Args:
        preco (int, optional): [description]. Defaults to 0.
        taxa (int, optional): [description]. Defaults to 0.
        formato (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    """
    r = preco + (preco * taxa/100)
    return r if formato is False else moeda(r) #retorna a formatação
   
def diminuir(preco=0, taxa=0, formato=False):
    r = preco + (preco * taxa/100)
    return r if formato is False else moeda(r)
    
def dobro(preco=0, formato=False):
    r = preco*2
    return r if formato is False else moeda(r)
    
def metade(preco=0, formato=False):
    r = preco / 2
    return r if formato is False else moeda(r)
    
def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')
    
    

#O método replace() é utilizado para 
#substituir um ou mais trechos em uma string. 
#Ele contém parâmetros para auxiliar a forma de substituição desse conteúdo. 
#Em Python, o tipo string é imutável, o que significa que quando ela é declarada, 
#não é possível realizar alterações em seu conteúdo.'''