l = float(input('Qual a largura da parede?'))
c = float(input('Qual o comprimento da parede?'))
m2 = l * c
tinta = m2 / 2
print('O tamanho da parede é de {}x{} ou {}m2 e você vai utilizar {} litros de tinta para pintar ela inteira'.format(l, c, m2, tinta))
