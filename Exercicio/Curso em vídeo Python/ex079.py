c = 0
lista = []
while True:
    c = (int(input('Digite um número: ')))
    if c not in lista:
        print('Número adicionado com sucesso.')
        lista.append(c)
    else:
        c = int(input('Número ja existe na lista, digite outro:'))
    sn = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if sn == 'N':
        break
lista.sort()
print('Você digitou esses valores {}'.format(lista))

