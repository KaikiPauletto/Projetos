import random
n = 0
lista = [0, 1, 2, 3, 4, 5]
count = 0
while True:
    n = int(input('Digite um valor: '))
    poui = str(input('Par ou Ímpar? [P/I]: '))
    pc = random.choice(lista)
    if poui == 'P' and (n + pc) % 2 == 0:
        print('Eu escolhi {}. Você ganhou!'.format(pc))
        count += 1
    if poui == 'I' and (n + pc) % 2 != 0:
        print('Eu escolhi {}. Você ganhou!'. format(pc))
        count += 1
    elif poui == 'P' and (n + pc) % 2 != 0 or poui == 'I' and (n + pc) % 2 == 0:
        print('Eu escolhi {}. Você perdeu! Você ganhou {} vezes seguidas'.format(pc, count))
        break


