velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade>80:
    print('Você está muito rápido o limite da via é 80km/h, voce deverá pagar uma multa de R${},00.'.format((velocidade - 80)* 7))
else:print('Ok tenha uma boa viagem!')

