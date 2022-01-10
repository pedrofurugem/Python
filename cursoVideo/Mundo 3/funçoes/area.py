def area(l, a):
    ar = l * a
    print(f'A area de um terreno {l}x{a} é {ar}m²')
    
    
#programa principal
larg = float(input('LARGURA (m): '))
alt = float(input('COMPRIMENTO (m): '))
area(larg, alt)