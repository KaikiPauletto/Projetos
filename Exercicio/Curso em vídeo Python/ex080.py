lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print('Adicionado na posição {} da lista'.format(pos))
                break
            pos += 1
print('-=' * 30)
print('Os valores digitados em fordem foram {}'.format(lista))
