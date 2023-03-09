valor = float(input('Qual o valor do produto? R$'))
pagamento = int(input('Qual será a forma de pagamento? \n[1] À vista/Cheque\n[2]À vista no cartão:\n[3]Até 2x no cartão\n[4]3x ou mais no cartão\nDigite o número de acordo com a forma de pagamento: '))
if pagamento == 1:
    print('O valor é de R${:.2f} mas como você vai pagar à vista ou no cheque você ganha 10% de desconto, ficando R${:.2f}'.format(valor, valor - (valor * 10 / 100)))
elif pagamento == 2:
    print('O valor é de R${:.2f} mas como você vai pagar à vista no cartão vocçe tem 5% de descont ficando R${:.2f}'.format(valor, valor - (valor * 5 / 100)))
elif pagamento == 3:
    print('O valor continua sendo R${}'.format(valor))
elif pagamento == 4:
    vezes = int(input('Em quantas vezes deseja pagar?'))
    total = valor + (valor * 20 / 100)
    pormes = total / vezes
    print('O valor é de R$ {} mas como você vai parcelar em {}x o valor fica de R${} ou seja R${} por mês'.format(valor, vezes, total, pormes))


