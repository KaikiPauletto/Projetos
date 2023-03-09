n = int(input('Digite que termo deseja encontrar: '))
penultimo = 1
ultimo = 1


if (n==1) or (n==2):
    print('1')
else:
    count = 3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print((termo), end=' - ')
print(('Fim'), end=' ')