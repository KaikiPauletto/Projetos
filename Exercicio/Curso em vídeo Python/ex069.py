idade = maioridade = masculinos = mulhersub20 = 0
sexo = ''
while True:
    idade = int(input('Qual a idade dessa pessoa? '))
    sexo = str(input('Qual o sexo dessa pessoa? [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        masculinos += 1
    if sexo == 'F' and idade < 20:
        mulhersub20 += 1
    positivo = str(input('Quer cadastrar mais alguém? [S/N]: ')).upper().strip()[0]
    if positivo == 'N':
        break
print('Tem {} pessoas com mais de 18 anos.'.format(maioridade))
print('Foram cadastrados {} homens.'.format(masculinos))
print('Tem {} mulheres com menos de 20 anos.'.format(mulhersub20))



