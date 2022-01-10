print('\033[31mOla mundo') #escrever em vermelho
print('\033[31;43mOla mundo') #com funco amarelo
print('\033[1;31;43mOla mundo') #em negrito
print('\033[1;31;43mOla mundo!\033[m') #encurtar a faixa
    #detalhe; letra; fundo      #fechar la letra
print('\033[4;30;45mOla mundo!\033[m') #sublinhado
print('\033[36mOla mundo!\033[m') #azul água
print('\033[7;30mOla mundo!\033[m') #inversão
# AQUI NO VSCODE não rola kkkkkkkkkkkkk

#conferir na imagem

#colocar cores nas variáveis
a = 31
b = 3
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!!!'.format(a, b))

#maneira simplificada


