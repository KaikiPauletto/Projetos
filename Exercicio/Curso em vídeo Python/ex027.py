n = str(input('Qual o seu nome completo?')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo sobrenome é {}'.format(nome[len(nome)-1]))
