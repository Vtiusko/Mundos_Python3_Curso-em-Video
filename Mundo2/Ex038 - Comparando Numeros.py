'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

	– O primeiro valor é maior
	– O segundo valor é maior
	– Não existe valor maior, os dois são iguais
'''

print('É MAIOR, MENOR ou os dois números são IGUAIS?')

num1 = int(input('\n\nPrimeiro número: '))
num2 = int(input('\nSegundo número: '))

if num1 > num2:
	print(f'\nO número {num1} é MAIOR que o número {num2}')
elif num1 < num2:
	print(f'\nO número {num2} é MAIOR que o número {num1}')
elif num1 == num2:
	print('\nAmbos os números são IGUAIS')	