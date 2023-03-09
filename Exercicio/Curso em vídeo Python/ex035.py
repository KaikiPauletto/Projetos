primeiro = float(input('Qual a medida do primeiro segmento?'))
segundo = float(input('Qual a medida do segundo seguimento?'))
terceiro = float(input('Qual a medida do terceiro segmento?'))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('O segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
