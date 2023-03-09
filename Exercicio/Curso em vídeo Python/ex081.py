lista = []
count = 0
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    count += 1
    sn = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if sn == 'N':
        break
if 5 in lista:
        print('O valor 5 foi digitado.')
else:
        print('O valor 5 não foi digitado.')
lista.sort(reverse=True)
print(lista)
print('Foram digitados {} números'.format(count))


