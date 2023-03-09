dias = float(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram percorridos?'))
c1 = dias * 60
c2 = km * 0.15
c3 = c1 + c2
print('O valor do aluguél ficará de R${:.2f}'.format(c3))
