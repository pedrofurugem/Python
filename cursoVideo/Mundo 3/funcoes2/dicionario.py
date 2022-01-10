def notas(* n, situacao=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando ou não se deve adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if situacao:
        if r['media'] >= 7.00:
            r['situacao'] = 'BOA'
        elif  r['media'] >= 5.00:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r
    
     
resp = notas(5.5, 6.5, 9, 8.5, situacao = True)
print(resp)
help(notas)