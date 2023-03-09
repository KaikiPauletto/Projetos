from datetime import date
dados = {}
atual = date.today().year
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = atual - nascimento
dados['carteira de trabalho'] = int(input('Carteira de Trabalho: [0 não tem]: '))
if dados['carteira de trabalho'] != 0:
    dados['contratação'] = int(input('Em que ano foi contratado? '))
    dados['salario'] = float(input('Qual o salário? '))
aposentadoria1 = dados['contratação'] + 35
aposentadoria2 = aposentadoria1 - atual
dados['aposentadoria'] = aposentadoria2 + dados['idade']
print('-=' * 40)
for k, v in dados.items():
    print('{} tem o valor {}'.format(k, v))





