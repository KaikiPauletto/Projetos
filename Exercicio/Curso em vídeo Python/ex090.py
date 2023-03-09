alunos = {}
nome = alunos['nome'] = str(input('Nome: '))
media = alunos['media'] = float(input('Média: '))
if media >= 7:
    alunos['situação'] = 'Aprovado'
elif media >= 5 and media < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
for k, v in alunos.items():
    print('{} é igual a {}'.format(k, v))
