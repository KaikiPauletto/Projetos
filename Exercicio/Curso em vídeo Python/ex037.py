num = int(input('Digite um número inteiro:'))
escolha = int(input('Digite (1) se deseja converter para binário. \nDigite (2) se deseja converter para octal \nDigite (3) se deseja converter para hexadecimal. \nNúmero escolhido:'))
if escolha == 1:
    print(bin(num))
elif escolha == 2:
    print(oct(num))
elif escolha == 3:
    print(hex(num))


