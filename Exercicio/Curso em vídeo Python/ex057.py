sexo = str(input('Digite o sexo [M/F]: ')).upper()
while sexo not in 'MF':     
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
    if sexo == 'M':
        print('Seu sexo é masculino')
    elif sexo == 'F':
        print('Seu sexo é feminino')




