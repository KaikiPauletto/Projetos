galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('A) Ao todo temos {} pessoas cadastradas'.format(len(galera)))
media = soma / len(galera)
print('B) A média de idade é de {:.2f} anos'.format(media))
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print('{}'.format(p["nome"]))
print()
print('D) Lista das pessos que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print('{} = {}'.format(k, v))
        print()
print('<<< ENCERRADO >>>')

