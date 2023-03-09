from datetime import date
nsc = int(input('Escreva o ano que você nasceu:'))
atual = date.today().year
idade = atual - nsc
if idade > 18:
    print('Já passou sua oportunidade.')
elif idade < 18: 
    print('Ainda faltam {} anos para você se alistar'.format(18 - idade))
elif idade == 18:
    print('Está na hora.')
    
