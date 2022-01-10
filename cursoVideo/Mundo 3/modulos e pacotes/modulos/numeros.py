#temos duas formas diferentes de importação
#todo arquivo do python pode ser um modulo
import uteis #forma mais recomendada
#from uteis import fatorial, dobro, triplo #essa forma não é muito recomendavel pois pode gerar conflito entre uma funão e outra

#função princípal
num = int(input('Digite um valor: '))
#fat = fatorial(num)
#dob = dobro(num)
#tri = triplo(num)
fat = uteis.fatorial(num)
dob = uteis.dobro(num)
tri = uteis.triplo(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dob}")
print(f"O triplo de {num} é {tri}")

##Vantagens##
#Organização do código
#Facilidade na manutenção
#ocultação de código detalhado
#Reutilização em outros projetos


