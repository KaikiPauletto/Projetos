altura = float(input('Qual a sua altura?'))
peso = float(input('Qual o seu peso?'))
calculo = altura * altura
calculo2 = peso / calculo
if calculo2 < 18.5:
    print('Seu IMC é de {:.1f} e você está abaixo do peso.'.format(calculo2))
elif calculo2 >= 18.5 and calculo2 < 25:
    print('Seu IMC é de {:.1f} e o seu peso está ideal.'.format(calculo2))
elif calculo2 >= 25 and calculo2 < 30:
    print('Seu IMC é de {:.1f} e você está com sobrepeso.'.format(calculo2))
elif calculo2 >= 30 and calculo2 < 40:
    print('Seu IMC é de {:.1f} e você está com obesidade.'.format(calculo2))
elif calculo2 >= 40:
    print('Seu IMC é de {:.1f} e você está com obesidade mórbita.'.format(calculo2))


