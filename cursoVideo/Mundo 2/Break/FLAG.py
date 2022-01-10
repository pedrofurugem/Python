cont = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f' Foram digitados {cont} numeros e a soma é igual a {s}')