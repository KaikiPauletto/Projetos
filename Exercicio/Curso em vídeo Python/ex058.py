import random
tentativas = 1
lst = list(range(1,10+1))
pc = random.choice(lst)
escolhido = int(input('Digite um número: '))
while escolhido != pc:
    if pc > escolhido:
        escolhido = int(input('mais... Tente outra vez: '))
    elif pc < escolhido:
        escolhido = int(input('menos... Tente outra vez: '))
    tentativas += 1
if pc == escolhido:
    print('Você acertou o número {} com {} tentativas'.format(pc, tentativas))
