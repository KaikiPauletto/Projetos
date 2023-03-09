time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input('    Quantos gols na partida {}?'.format(c+1))))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas com S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com o código {}!'.format(busca))
    else:
        print('-- LEVANTAMENTO DO JOGADOR {} --'.format(time[busca]["nome"]))
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')


