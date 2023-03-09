from time import sleep
from random import randint
from operator import itemgetter
jogador = {}
jogador1 = randint(0, 6)
jogador2 = randint(0, 6)
jogador3 = randint(0, 6)
jogador4 = randint(0, 6)
jogador['jogador1'] = jogador1
jogador['jogador2'] = jogador2
jogador['jogador3'] = jogador3
jogador['jogador4'] = jogador4
ranking = []
for k, v in jogador.items():
    print('{} tirou {}'.format(k, v))
    sleep(1)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('-=-=-=- RANKING DOS JOGADORES -=-=-=-')
for i, v in enumerate(ranking):
    print('{}° lugar: {} com {}'.format(i+1, v[0], v[1]))
    sleep(1)



