km = float(input('Qual a distância da viagem?'))
if km<=200:
    print('O custo da viagem foi de R${:.2f}'.format(km * 0.50))
else:
    print('O custo da viagem foi de R${:.2f}'.format(km * 0.45))


