def voto(idade):
    from datetime import date 
    atual = date.today().year
    idade = atual - ano
    if idade >= 18 and idade < 65: #usei o 'and'
        return f'com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 16:
        return f'com {idade} anos: VOTO OPCIONAL'
    else:
        return f'com {idade} anos: VOTO NEGADO'
      
ano = int(input('Em que ano você nasceu? ')) 
print(voto(ano))
