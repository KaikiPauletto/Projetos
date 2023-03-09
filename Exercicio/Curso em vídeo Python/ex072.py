numeros = ('zero', 'um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 
            'Dezesseis', 'Dezessete', 'Dezoito','Dezenove', 'Vinte') 
escolha = int(input('Digite um número de 0 a 20: '))
if escolha < 0:
    print('Tente novamente.')
    escolha = int(input('Digite um número de 0 a 20: '))
elif escolha > 20:
    print('Tente novamente.')
    escolha = int(input('Digite um número de 0 a 20: '))
print(numeros[escolha])
