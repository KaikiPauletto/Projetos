from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1,8):
    ano = int(input('Digite o ano que a {}a pessoa nasceu: '.format(c))) 
    calculo = atual - ano
    if calculo >= 18:
        maiores += 1
    else:
        menores += 1
print('Das 7 pessoas {} são maiores de idade'.format(maiores))
print('E tivemos {} menores de idade.'.format(menores))

