tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico Paranaense', 
            'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América Mineiro', 'Botafogo', 'Santos', 
            'Goias', 'Bragantino', 'Coritiba', 'Cuiaba', 'Ceara', 'Atlético Goianiense', 'Avaí', 'Juventude')
ordem = sorted(tabela)
print('=-'*100)
print(tabela)
print('=-'*100)
print(tabela[:6])
print('=-'*100)
print(tabela[16:])
print('=-'*100)
print(ordem)
print('=-'*100)
print('Internacional está na posição {}'.format(tabela.index('Internacional') + 1))
print('=-'*100)
print('Fim')


