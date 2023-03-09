import random
from time import sleep
print('====VOU PENSAR EM UM NÚMERO ENTRE 0 E 5... DUVIDO VOCÊ ADIVINHAR!!!')
nu = int(input('Chute um número: '))
lista = [0, 1, 2, 3, 4, 5]
nc = random.choice(lista)
print('PROCESSANDO...')
sleep(2)
if nc == nu:
    print('Parabéns eu pensei no número {} também'.format(nu))
else:
    print('Você errou! Eu pensei em {}'.format(nc))

