#programa para aprovar o emrestimo bancario para a compra de uma casa

valor = float(input('digite o valor da casa: '))
salario = float(input('digite o valor do salario do comprador: '))
anos = int(input('em quantos anos pretende pagar: '));

print('valor da casa: R${:.2f}'.format(valor))
print('salario: R${:.2f}'.format(salario))
print('anos a pagar: {}'.format(anos))

prestacao = valor / (anos * 12)
s30 = salario * 30/100
print('o valor da prestação mensal é de R${:.2f}'.format(float(prestacao)))    

if prestacao <= s30:   
    print('o emprestimo pode ser concedido para o salario de R${:.2f} e a prestação mensal de R${:.2f}'.format(salario, prestacao))
else: 
    print('EMPRESTIMO NEGADO')