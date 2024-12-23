'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

	A fórmula para calcular qualquer termo de uma PA é: an = a1 + (n-1)r . Onde `an` é o termo que queremos calcular, `a1` é o primeiro termo da PA, `n` é a posição do termo que queremos descobrir e `r` é a razão.

		- `an`: É o termo que queremos calcular. Por exemplo, se quisermos calcular o quinto termo de uma PA, `an` seria `a5`.
		- `a1`: É o primeiro termo da PA. Por exemplo, na PA (2, 4, 6, 8), o primeiro termo é 2.
		- `n`: É a posição do termo que queremos descobrir. Por exemplo, se quisermos calcular o quinto termo de uma PA, `n` seria igual a 5.
		- `r`: É a razão da PA. A razão é a diferença constante entre dois termos consecutivos da PA. Por exemplo, na PA (2, 4, 6, 8), a razão é 2.

	Vamos usar um exemplo para entender melhor como usar essa fórmula. Suponha que queremos calcular o quinto termo da PA (2, 4, 6, 8). Podemos usar a fórmula: a5 = 2 + (5-1)2 = 10. Nesse caso:

		- `an` é igual a `a5`, porque queremos calcular o quinto termo da PA.
		- `a1` é igual a 2, porque o primeiro termo da PA é 2.
		- `n` é igual a 5, porque queremos calcular o quinto termo da PA.
		- `r` é igual a 2, porque a razão da PA é 2.

	Substituindo esses valores na fórmula, temos: a5 = 2 + (5-1)2 = 10. Então, o quinto termo da PA é 10.
'''
from tabulate import tabulate
from time import sleep
from os import system, name
from tqdm import tqdm
from sys import stdout

def apresentacao():
	print('{:=^51}'.format(' DESCUBRA QUAL É A PA '))
	print(f'\033[3;36m{"A fórmula é: AN = A1 + (N - 1)R":^51}\033[m')

def opcoes():
	print('\n\n{:^51}'.format('Caso não lembre, precisamos de algumas informações:'))	
	A1 = int(input('\nDefina "\033[36mA1\033[m" (primeiro número): ').strip())
	R = int(input('\nDefina "\033[36mR\033[m" (razão / Ex: 2 em 2...): ').strip())
	N = int(input('\nDefina "\033[36mN\033[m" (posição do termo): ').strip())	
	
	print('\n\033[1;4m{:^36}\033[m'.format('T A B E L A   D E   O P Ç Õ E S:'))
	opcoes = [
		['\033[36m[ 1 ]\033[m', '10 primeiros termos'],
		['\033[36m[ 2 ]\033[m', '100 primeiros termos'],
		['\033[36m[ 3 ]\033[m', '1000 primeiros termos'],
		['\033[36m[ 4 ]\033[m', 'Executar Cálculo'],
		['\033[36m[ 5 ]\033[m', 'Redefinir termos'],
		['\033[36m[ 6 ]\033[m', 'Encerrar o Programa']
	]

	print(tabulate(opcoes, headers=['OPÇÕES','DESCRIÇÕES'], tablefmt='orgtbl'))
	return A1, R, N

def loading_animation(num_times):
    animacao = ['-', '\\', '|', '/']
    contador = 0
    while contador < num_times:
        for simbolo in animacao:
            stdout.write('\rCarregando... ' + simbolo)
            stdout.flush()
            sleep(0.1)
        contador += 1
        stdout.write('\r\033[36mCarregado!\033[m     ')      

def finish_animation(num_times):
    animacao = ['-', '\\', '|', '/']
    contador = 0
    while contador < num_times:
        for simbolo in animacao:
            stdout.write('\rFinalizando... ' + simbolo)
            stdout.flush()
            sleep(0.1)
        contador += 1
        stdout.write('\r\033[36mFinalizado!\033[m     ')

def banner():
	print('{:=^51}'.format(' DESCUBRA QUAL É A PA '))
	print('\033[3;36m{:^51}\033[m'.format('A fórmula é: AN = A1 + (N - 1)R'))

menu_opcoes = {1: 'Redefinir "\033[36mN\033[m" (Ex: 189° posição)', 2: 'Redefinir "\033[36mR\033[m" (Ex: 356 em 356, 2 em 2...', 3: 'Redefinir "\033[36mA1\033[m" (início / começo / 1° número)'} # Itens da opção 4

apresentacao()
A1, R, N = opcoes()

while True:
	opc = int(input('\nEscolha uma opção: '))
	if opc == 1:
		loading_animation(5) # fornece o argumento num_times
		sleep(1)
		system('cls' if name == 'nt' else 'clear')
		banner()	
		N = 10
		AN = A1 + (N - 1) * R
		num_digitos = len(str(AN))
		print(f'\n \033[36m》\033[m  A{N} \033[36m=\033[m {A1} \033[36m+\033[m ({N} \033[36m-\033[m 1) \033[36m*\033[m {R}')
		print(f' \033[36m》\033[m  A{N} \033[36m=\033[m {AN}')
		mostrar_progressao = str(input('\nDeseja ver a progressão completa \033[36m[\033[m S \033[36m/\033[m N \033[36m]\033[m? ').strip())
		loading_animation(5)
		print('\n')
		if mostrar_progressao.lower() == 's':
			for i in range(N):
				termo = A1 + i * R
#. Essa linha print faz com que o número se muito elevado,
#. Se ajuste automaticamente ao espaço,
#. Pra ficar uma coisa mais estética.
				print('{:^{}}'.format(termo, num_digitos), end=' \033[33m>\033[m ' if i < N - 1 else '.')
	elif opc == 2:
		loading_animation(5) # fornece o argumento num_times
		sleep(1)
		system('cls' if name == 'nt' else 'clear')
		banner()	
		N = 100
		AN = A1 + (N - 1) * R
		num_digitos = len(str(AN))
		print(f'\n \033[36m》\033[m  A{N} \033[36m=\033[m {A1} \033[36m+\033[m ({N} \033[36m-\033[m 1) \033[36m*\033[m {R}')
		print(f' \033[36m》\033[m  A{N} \033[36m=\033[m {AN}')
		mostrar_progressao = str(input('\nDeseja ver a progressão completa \033[36m[\033[m S \033[36m/\033[m N \033[36m]\033[m? ').strip())
		loading_animation(5)
		print('\n')
		if mostrar_progressao.lower() == 's':
			for i in range(N):
				termo = A1 + i * R
				print('{:^{}}'.format(termo, num_digitos), end=' \033[33m>\033[m ' if i < N - 1 else '.')
	elif opc == 3:
		loading_animation(5) # fornece o argumento num_times
		sleep(1)
		system('cls' if name == 'nt' else 'clear')
		banner()
		N = 1000
		AN = A1 + (N - 1) * R
		num_digitos = len(str(AN))
		print(f'\n \033[36m》\033[m  A{N} \033[36m=\033[m {A1} \033[36m+\033[m ({N} \033[36m-\033[m 1) \033[36m*\033[m {R}')
		print(f' \033[36m》\033[m  A{N} \033[36m=\033[m {AN}')
		mostrar_progressao = str(input('\nDeseja ver a progressão completa \033[36m[\033[m S \033[36m/\033[m N \033[36m]\033[m? ').strip())
		loading_animation(5)
		print('\n')
		if mostrar_progressao.lower() == 's':
			for i in range(N):
				termo = A1 + i * R
				print('{:^{}}'.format(termo, num_digitos), end=' \033[33m>\033[m ' if i < N - 1 else '.')		
	elif opc == 4:
		loading_animation(5) # fornece o argumento num_times
		sleep(1)
		system('cls' if name == 'nt' else 'clear')
		banner()
		AN = A1 + (N - 1) * R
		num_digitos = len(str(AN))
		print(f'\n \033[36m》\033[m  A{N} \033[36m=\033[m {A1} \033[36m+\033[m ({N} \033[36m-\033[m 1) \033[36m*\033[m {R}')
		print(f' \033[36m》\033[m  A{N} \033[36m=\033[m {AN}')
		mostrar_progressao = str(input('\nDeseja ver a progressão completa \033[36m[\033[m S \033[36m/\033[m N \033[36m]\033[m? ').strip())
		loading_animation(5)
		print('\n')
		if mostrar_progressao.lower() == 's':
			for i in range(N):
				termo = A1 + i * R
				print('{:^{}}'.format(termo, num_digitos), end=' \033[33m>\033[m ' if i < N - 1 else '.')
	elif opc == 5:
		loading_animation(5) # fornece o argumento num_times
		sleep(1)
		system('cls' if name == 'nt' else 'clear')
		banner()
		print('')
		for opcao, descricao in menu_opcoes.items():
		   print(f'\033[36m[\033[m {opcao} \033[36m]\033[m - {descricao}')

		opcoes = int(input('\nSelecione uma opção: '))
		if opcoes == 1:
			N = int(input('\nRedefina o valor de "\033[36mN\033[m": '))
		if opcoes == 2:
			R = int(input('\nRedefina o valor de "\033[36mR\033[m": '))
		if opcoes == 3:
			A1 = int(input('\nRedefina o valor de "\033[36mA1\033[m": '))
		
		system('cls' if name == 'nt' else 'clear')
		banner()
		
		AN = A1 + (N - 1) * R
		
		num_digitos = len(str(AN))
		
		print(f'\n \033[36m》\033[m  A{N} \033[36m=\033[m {A1} \033[36m+\033[m ({N} \033[36m-\033[m 1) \033[36m*\033[m {R}')
		print(f' \033[36m》\033[m  A{N} \033[36m=\033[m {AN}')
		mostrar_progressao = str(input('\nDeseja ver a progressão completa \033[36m[\033[m S \033[36m/\033[m N \033[36m]\033[m? ').strip())
		loading_animation(5)
		print('\n')
		if mostrar_progressao.lower() == 's':
			for i in range(N):
				termo = A1 + i * R
				print('{:^{}}'.format(termo, num_digitos), end=' \033[33m>\033[m ' if i < N - 1 else '.')
	elif opc == 6:
		system('cls' if name == 'nt' else 'clear')
		finish_animation(5)
		print('\n\nAté mais!')
		break 	
	perg = str(input('\n\nDeseja calcular novamente \033[36m[\033[m S \033[36m/\033[m N \033[36m]\033[m? ').strip())
	if perg.upper() == 'S':
		loading_animation(5)
		system('cls' if name == 'nt' else 'clear')
		print('{:=^51}'.format(' DESCUBRA QUAL É A PA '))
		print('\033[3;36m{:^51}\033[m'.format('A fórmula é: AN = A1 + (N - 1)R'))
		print('\n')
		opcoes = [
		['\033[36m[ 1 ]\033[m', '10 primeiros termos'],
		['\033[36m[ 2 ]\033[m', '100 primeiros termos'],
		['\033[36m[ 3 ]\033[m', '1000 primeiros termos'],
		['\033[36m[ 4 ]\033[m', 'Executar Cálculo'],
		['\033[36m[ 5 ]\033[m', 'Redefinir termos'],
		['\033[36m[ 6 ]\033[m', 'Encerrar o Programa']
	]
		print(tabulate(opcoes, headers=['OPÇÕES','DESCRIÇÕES'], tablefmt='orgtbl'))		
	else:
		system('cls' if name == 'nt' else 'clear')
		finish_animation(5)
		print('\n\nAté mais!')
		break
