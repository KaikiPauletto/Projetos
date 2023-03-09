num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite o {}o valor: '.format(c)))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort
num[1].sort
print('Números pares: {}'.format(num[0]))
print('Números ímpares: {}'.format(num[1]))

