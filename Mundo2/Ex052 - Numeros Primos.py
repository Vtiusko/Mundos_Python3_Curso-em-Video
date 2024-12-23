'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

- Números primos são números que possuem apenas "dois" divisores.

- Números compostos são números que possuem "tres" ou mais divisores.
'''
from time import sleep

n = int(input('Informe um número pra saber se é "PRIMO": '))
div = 0
print('')

for v in range(1, n + 1):
	if n % v == 0:
		print('\033[37m', end='')
		div +=1
	else:
		print('\033[31m', end='')
	print('{} \033[m'.format(v), end='')
	

print('\n\n- O número \033[37m{}\033[m foi divisível \033[37m{}\033[m vezes.'.format(n, div))

if div != 2:
	print('\n- O número: {}, \033[31mNÃO\033[m é primo!'.format(n))
else:
	print('\n- O número: {}, \033[32mÉ\033[m primo!'.format(n))
