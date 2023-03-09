from time import sleep
valor1 = 0
valor2 = 0
opçao = 0
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
while opçao != 5:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Processando...')
    sleep(1)
    print('[1] SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA')
    opçao = int(input('Qual sua opção? '))
    if opçao == 1:
        mais = valor1 + valor2
        print('{} + {} = {}'.format(valor1, valor2, mais))
    elif opçao == 2:
        multi = valor1 * valor2
        print('{} X {} = {}'.format(valor1, valor2, multi))
    elif opçao == 3:
        if valor1 > valor2:
            print('O maior valor é {}'.format(valor1))
        else:
            print('O maior valor é {}'.format(valor2))
    elif opçao == 4:
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite um novo valor: '))
    elif opçao == 5:
        print('Seu programa foi encerrado.')
        break


