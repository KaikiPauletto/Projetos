n1 = int(input('Digite um número que você deseja saber a tabuada: '))
while True:
    for c in range(0, 11):
        print('{} x {} = {}'.format(n1, c, n1*c))
    n1 = int(input('Digite outro número: '))
    if n1 < 0:
        print('FIM')
        break



