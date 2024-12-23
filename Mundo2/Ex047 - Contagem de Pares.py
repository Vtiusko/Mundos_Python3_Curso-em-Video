'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

# - % = Resto da divisao, o que sobra.
# - // = Resto da divisao inteira (debaixo da chave).

print('Num. Pares:\n')

num = 0

for n in range(2, 51, 2):
# Mostra quais sao os numeros pares
	print(n, end=' ')
# Mostra quantos numeros pares tem
	num += n % 2 == 0

print('\n\nAo todo sao {} numeros pares.'.format(num))