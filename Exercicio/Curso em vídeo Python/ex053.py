frase = str(input('Digite uma frase: ')).strip()
palavras = frase.split()
invertido = frase[::-1]
palavras2 = invertido.split()
junto = ''.join(palavras)
junto2 = ''.join(palavras2)
maiusculas1 = junto.upper()
maiusculas2  = junto2.upper()
print('A sua frase é {} e invertida fica {}'.format(maiusculas1, maiusculas2))
if maiusculas1 == maiusculas2:
    print('Essa palavra é um palindromo')
else:print('Essa palavra não é um palindromo')
