from random import randint
from time import sleep
print('Faça sua jogada')
vc = int(input('[1] PEDRA\n[2] PAPEL\n[3] TESOURA\nQual sua escolha?'))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!')
sleep(0.7)
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
if computador == 0 and vc == 1:
    print('Houve um empate, nós dois escolhemos PEDRA.')
elif computador == 1 and vc == 1:
    print('Eu ganhei, escolhi PAPEL e você escolheu PEDRA.')
elif computador == 2 and vc == 1:
    print('Você ganhou eu escolhi TESOURA e você escolheu PEDRA.')
elif computador == 0 and vc == 2:
    print('Você ganhou eu escolhi PEDRA e você escolheu PAPEL.')
elif computador == 1 and vc == 2:
    print('Houve um empate, nós dois escolhemos PAPEL.')
elif computador == 2 and vc == 2:
    print('Eu ganhei, eu escolhi TESOURA e você escolheu PAPEL.')
elif computador == 0 and vc == 3:
    print('Eu ganhei, eu escolhi PEDRA e você escolheu TESOURA.')
elif computador == 1 and vc == 3:
    print('Você ganhou eu escolhi PAPEL e você escolheu TESOURA.')
elif computador == 2 and vc == 3:
    print('Houve um empate, nós dois escolhemos TESOURA.')









