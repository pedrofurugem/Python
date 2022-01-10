print('LOJA')
preco = float(input('informe o preco da compra: R$ '))
print('escolha uma forma de pagamento')
print('[1] = à vista dinheiro/cheque')
print('[2] = à vista cartão')
print('[3] = em até 2x no cartão')
print('[4] = 3x ou mais no cartão')

tipo = int(input('informe o tipo de pagamento: '))

if tipo == 1: 
    print('à vista dinheiro/cheque')
    desconto = preco * (10/100)
    valor = preco - desconto
    print('valor de R${:.2f} com desconto de 10%'.format(valor))
elif tipo == 2: 
    print('à vista cartão')
    desconto = preco * (5/100)
    valor = preco - desconto
    print('valor de R${:.2f} com desconto de 5%'.format(valor))
elif tipo == 3:
    parcelas = preco / 2
    print('em até 2x no cartão sem juros')
    print('preço normal')
    print('R${:.2f} em duas vezes de R${}'.format(preco, parcelas))
elif tipo == 4:
    print('3x ou mais no cartão')
    print('20% de juros')
    parcelas = int(input('em quantas parcelas você quer? '))
    juros = preco * (20/100)
    precoJuros = preco + juros
    valorParcelado = precoJuros / parcelas
    print('O valor sera de R${:.2f} em {} vezes de R${:.2f}'.format(precoJuros, parcelas, valorParcelado))
else:
    print('OPÇÃO INVALIDA! digite uma das opções de 1 a 4 ')