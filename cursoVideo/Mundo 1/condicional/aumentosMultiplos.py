salario = float(input('Qual o valor do seu salario? '))
print('meu salario é de R${:.2f}'.format(salario))
aumento = int

if salario > 1250.00:
   aumento = salario * 10/100
   valorfinal = aumento + salario
   print('seu aumento é de R${:.2f}'.format(aumento))
   print('seu salario liquido é de R${:.2f}%'.format(valorfinal))
else: 
   aumento = salario * 15/100
   valorfinal = aumento + salario
   print('seu aumento é de R${:.2f}'.format(aumento))
   print('seu salario liquido é de R${:.2f}'.format(valorfinal))