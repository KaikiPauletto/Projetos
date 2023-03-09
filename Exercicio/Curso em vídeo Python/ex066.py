n= 0
count = 0
soma = 0
while True:
    n = int(input('Digite um número [999 para parar]'))
    if n == 999:
        break
    count += 1
    soma += n
print('Foram digitados {} numeros e a soma entre eles vale {}'.format(count, soma))
