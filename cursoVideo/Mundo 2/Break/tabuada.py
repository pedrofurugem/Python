print('-------------TABUADA---------------')
cont = 1
while True:
    n = int(input('informe qualquer número para calculo de tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        t = c * n
        cont += 1
        print(f'{n} X {c} = {t}')
print('Tabuada de número negativo não')
print('FIM')