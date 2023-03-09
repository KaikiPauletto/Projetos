co = float(input('Qual é o comprimento do cateto oposto?'))
ca = float(input('Qual é o comprimento do cateto adjacente?'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
