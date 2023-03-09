salário = float(input('Qual o salário do funcionário?'))
aumento = salário + (salário * 15 / 100)
print('Com o aumento salarial o salario foi de {} para {:.2f}'.format(salário, aumento))
