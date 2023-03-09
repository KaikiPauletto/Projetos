soma = count = n = 0
n = int(input('Digite um número: [999 para parar] '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um número: [999 para parar] '))
print('forma digitados {} números e a soma entre eles é de {}.'.format(count, soma))



