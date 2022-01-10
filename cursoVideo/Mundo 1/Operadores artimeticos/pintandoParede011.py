larg = float(input('digite a largura da parede: '))
alt = float(input('digite a altura da parede: '))

area = larg * alt
tinta = area / 2
print('a parede de area {}m² precisa de {:.2f}L de tinta'.format(area, tinta))


