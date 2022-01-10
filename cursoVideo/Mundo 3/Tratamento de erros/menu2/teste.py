from menu import menu, cabecalho, leiaInt #só usar o from
from arquivo import arquivoExiste, criarArquivo, lerArquivo, cadastrar
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #função de listar conteúdo
        lerArquivo(arq)
    elif resposta == 2:
        #função para cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! digite uma opção válida!\033[m')
    sleep(2)