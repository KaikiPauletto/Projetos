r1 = float(input('Qual o comprimento do primeiro lado?'))
r2 = float(input('Qual o comprimento do segundo lado?'))
r3 = float(input('Qual o comprimento do terceiro lado?'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Isso pode formar um triângulo, ', end='')
    if r1 == r2 and r1 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO')
else:
    print('Isso não pode formar um triângulo')




