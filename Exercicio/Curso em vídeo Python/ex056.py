masculino = 0
feminino = 0
idadeTotal = 0
mulheresSub20 = 0
nomeVelho = ''
idadeVelho = 0
for nis in range(1, 5):
    print('------ {} Pessoa ------'.format(nis))
    nome = input('Qual é o seu nome?')
    idade = int(input('Qual a sua idade?'))
    sexo = input('Qual seu sexo?')
    idadeTotal += idade
    if sexo == 'M':
        masculino += 1
        if idade > idadeVelho:
            nomeVelho = nome
            idadeVelho = idade
    elif sexo == 'F':
        feminino += 1
        if idade <= 20:
            mulheresSub20 += 1
print('A média de idade é {}'.format(idadeTotal / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeVelho, nomeVelho))
print('Tem {} mulheres abaixo de 20 anos.'.format(mulheresSub20))
