nome = str(input('Digite seu nome completo:'))
maiusculas = (nome.upper())
minusculas = (nome.lower())
nomeSP = nome.replace(' ', '')
quantidade = len(nomeSP)
primeiro = nome.split()
print('De acordo com o nome {}.'.format(nome))
print('Em letras maiúsculas fica: {}.'.format(maiusculas))
print('Em letras minúsculas fica: {}.'.format(minusculas))
print('Seu nome tem {} letras sem considerar espaços.'.format(quantidade))
print('O seu primeiro nome tem {} letras.'.format(len(primeiro[0])))


