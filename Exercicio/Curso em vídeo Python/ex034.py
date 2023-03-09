salario = float(input('Qual o salário do funcionário? R$'))
aumento1 = (salario * 10 / 100) + salario
aumento2 = (salario * 15 / 100) + salario
if salario >= 1250.00:
    print('Com o aumento o salário fica R${:.2f}'.format(aumento1))
else:
    print('Com o aumento o salário fica R${:.2f}'.format(aumento2))


