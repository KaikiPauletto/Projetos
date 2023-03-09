jogador = {}
partidas = []
jogador['nome'] = str(input('Digite o nome do jogador: '))
tot = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
for c in range(0, tot):
    partidas.append(int(input('    Quantos gols na partida {}?'.format(c))))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print('{} tem o valor {}'.format(k, v))
print('-=' * 30)
print('O jogador {} jogou {} partidas'.format(jogador["nome"], len(jogador["gols"])))
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'foi um total de {jogador["total"]} gols.')