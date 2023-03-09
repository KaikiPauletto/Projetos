soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro:'))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma desses {} números pares é igual a {}'.format(cont, soma))

