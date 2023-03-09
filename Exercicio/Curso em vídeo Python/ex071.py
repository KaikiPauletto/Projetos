valor = int(input('Quanto você deseja sacar? '))
notas50 = valor // 50 
notas20 = valor % 50 // 20
notas10 = valor % 50 % 20 // 10
notas1 = valor % 50 % 20 % 10 // 1
print('{} cédulas de R$50,00'.format(notas50))
print('{} cédulas de R$20,00'.format(notas20))
print('{} cédulas de R$10,00'.format(notas10))
print('{} moedas de R$1,00'.format(notas1))


