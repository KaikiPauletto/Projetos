m = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)
for pos in range(0, len(m)):
    if pos % 2 == 0:
        print(f'{m[pos]:.<30}', end='')
    else:
        print(f'R${m[pos]:>7.2f}')

