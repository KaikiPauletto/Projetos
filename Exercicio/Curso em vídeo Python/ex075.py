num = (int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')))
print('Você digitou os valores {}'.format(num))
print('O valor 9 apareceu {} vezes'.format(num.count(9)))
if 3 in num:
    print('O número 3 aparece na posição {}'.format(num.index(3)+ 1))
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



