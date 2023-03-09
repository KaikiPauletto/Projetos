valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você deseja pagar essa casa?'))
porano = valor / anos
pormes = porano / 12
if (salario * 30 / 100) > pormes:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} por mês \n EMPRÉSTIMO CONCEDIDO!'.format(valor, anos, pormes))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} por mês \n EMPRÉSTIMO NEGADO!'.format(valor, anos, pormes))



