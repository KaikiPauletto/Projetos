media = 0
lista = []
num = 0
resposta = ''
count = 0
while resposta != 'N':
    num = int(input('Digite um valor: '))
    resposta = str(input('Quar continuar? [S/N]: ')).upper().strip()[0]
    count += 1
    media += num
    lista.append(num)
    if resposta == 'N':
        print('A média desses valores é de {}, o valor mais alto é {} e o mais baixo {}.'.format(media / count, max(lista), min(lista)))
    elif resposta != 'S' or 'N':
        print('Programa Inválido.')


