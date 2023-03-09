import random
primeiro = str(input('Qual o primeiro aluno?'))
segundo = str(input('Qual o segundo aluno?'))
terceiro = str(input('Qual é o terceiro aluno?'))
quarto = str(input('Qual é o quarto aluno?'))
lista = [primeiro, segundo, terceiro, quarto]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
