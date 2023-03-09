mai = 0
men = 0
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor para a posição {}:'.format(c))))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('Você digitou os valores {}'.format(valores))
print('O maior valor digitado foi {} nas posições '.format(mai), end='')
for i, v in enumerate(valores):
    if v == mai:
        print('{}...'.format(i), end='')
print()
print('O menor valor digitado foi {} nas posições '.format(men), end='')
for i, v in enumerate(valores):
    if v == men:
        print('{}...'.format(i), end='')
print()







