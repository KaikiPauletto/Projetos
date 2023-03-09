nome = ''
preço = 0
continuar = ''
cont = 0
total = 0
preçobarato = 1000
nomebarato = ''
while True:
    nome = str(input('Qual o nome do produto?'))
    preço = float(input('Qual o preço? R$'))
    continuar = str(input('Quer continuar? [S/N]: '))
    total += preço
    if preço >= 1000:
        cont += 1
    if preço < preçobarato:
        nomebarato = nome
        preçobarato = preço
    if continuar == 'N':
        break
print('O total gasto foi R${:.2f}'.format(total))
print('{} produtos custam mais de R$1000,00'.format(cont))
print('{} é a compra mais barata'.format(nomebarato))




