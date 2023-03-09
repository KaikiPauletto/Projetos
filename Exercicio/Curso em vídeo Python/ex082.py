lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um número: '))
    sn = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if n % 2 == 0:
        lista.append(n)
        listapar.append(n)
    if n % 2 == 1:
        lista.append(n)
        listaimpar.append(n)
    if sn == 'N':
        break
print('A lista inteira é {}'.format(lista))
print('A lista de números ímpares é {}'.format(listaimpar))
print('A lista de números pares é {}'.format(listapar))

