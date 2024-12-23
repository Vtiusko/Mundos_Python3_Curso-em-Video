'''
CONVERSOR DE BASE NUMÉRICA

Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

print('coversor de base numérica'.title())
num = int(input('\nDigite um número para ser convertido: '))
opcao = float(input('\nOpções:\n\n1 - Para BINÁRIO\n2 - Para OCTAL\n3 - Para HEXADECIMAL\n\nSelecione a opção desejada: '))

# base_BINÁRIA = bin(num)
# base_OCTAL = oct(num)
# base_HEXADECIMAL = hex(num)

if opcao == 1:
	print('\nO número {} em BINÁRIO: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
	print('\nO número {} em OCTAL: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
	print('\nO número {} em HEXADECIMAL: {}'.format(num, hex(num)[2:]))
elif opcao != '123':
	print('\nSelecione uma opção válida!')
	
'''
Aplicamos a regra de FATIAMENTO de strings, onde pedimls que ele print à partir do terceiro elemento da lista, ou segundo elemento da conversão:

	- [2:] = comece do terceiro item da lista até o final.
'''
