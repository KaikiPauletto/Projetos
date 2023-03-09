from datetime import date
ano = int(input('Digite o ano em que você nasceu:'))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação:MIRIM')
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação:INFANTIL')
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação:JÚNIOR')
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação:SÊNIOR')
elif idade > 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação:MASTER')
    

