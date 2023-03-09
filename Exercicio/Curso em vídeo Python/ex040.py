n1 = float(input('Qual foi a primeira nota?'))
n2 = float(input('Qual foi a segunda nota?'))
media1 = n1 + n2
media = media1 / 2
if media >= 7.0:
    print('Sua média foi de {:.1f} e você passou de ano.'.format(media))
elif media >= 5.0 and media < 7.0:
    print('Sua média foi de {:.1f} e você ficou de recuperação.'.format(media))
elif media < 5.0:
    print('Sua média foi de {:.1f} e você foi reprovado.'.format(media))
