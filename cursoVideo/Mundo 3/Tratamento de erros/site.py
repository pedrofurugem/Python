import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLERrror:
    print('o site pudim não esta acessivel no momento')
else:
    print('Acessado com sucesso')
    #print(site.read()) #lê o conteúdo de codigos do site