'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

import curses
from time import sleep
from concurrent.futures import ThreadPoolExecutor

def apresentacao(stdscr):
	stdscr.addstr(0, 0, '{:=^51}'.format(' DESCUBRA QUAL É A PA '))
	stdscr.addstr(1, 0, '{:^51}'.format('A fórmula é: AN = A1 + (N - 1)R'), curses.A_REVERSE)

def opcoes(stdscr):
	stdscr.addstr(3, 0, '{:^51}'.format('Caso não lembre, precisamos de algumas informações:'))
	stdscr.addstr(5, 0, 'Defina "A1" (primeiro número): ')
	curses.echo()
	A1 = int(stdscr.getstr())
	stdscr.addstr(6, 0, 'Defina "R" (razão / Ex: 2 em 2...): ')
	R = int(stdscr.getstr())
	stdscr.addstr(7, 0, 'Defina "N" (posição do termo): ')
	N = int(stdscr.getstr())
	curses.noecho()
	stdscr.addstr(9, 0, '{:^36}'.format('T A B E L A   D E   O P Ç Õ E S:'), curses.A_UNDERLINE)
	opcoes = [
		'[ 1 ] - 10 primeiros termos',
		'[ 2 ] - 100 primeiros termos',
		'[ 3 ] - 1000 primeiros termos',
		'[ 4 ] - Executar Cálculo',
		'[ 5 ] - Redefinir termos',
		'[ 6 ] - Encerrar o Programa'
	]
	for i, opcao in enumerate(opcoes):
		stdscr.addstr(11 + i, 0, opcao)
	return A1, R, N

def loading_animation(stdscr):
	animacao = ['-', '\\', '|', '/']
	for simbolo in animacao:
		stdscr.addstr(20, 0, 'Carregando... ' + simbolo)
		stdscr.refresh()
		sleep(0.1)
	stdscr.addstr(20, 0, 'Carregado!     ')

def finish_animation(stdscr):
	animacao = ['-', '\\', '|', '/']
	for simbolo in animacao:
		stdscr.addstr(20, 0, 'Finalizando... ' + simbolo)
		stdscr.refresh()
		sleep(0.1)
	stdscr.addstr(20, 0, 'Finalizado!     ')

def calcular_PA(stdscr):
	apresentacao(stdscr)
	A1, R, N = opcoes(stdscr)
	while True:
		stdscr.addstr(18, 0, 'Escolha uma opção: ')
		opc = int(stdscr.getch()) - ord('0')
		if opc == 1:
			loading_animation(stdscr)
			sleep(1)
			stdscr.clear()
			apresentacao(stdscr)
			N = 10
			AN = A1 + (N - 1) * R
			num_digitos = len(str(AN))
			stdscr.addstr(3, 0, f'》A{N} = {A1} + ({N} - 1) * {R}')
			stdscr.addstr(4, 0,f'》A{N} = {AN}')
			stdscr.addstr(6, 0,'Deseja ver a progressão completa [ S / N ]? ')
			mostrar_progressao = str(stdscr.getch(), 'utf-8')
			loading_animation(stdscr)
			if mostrar_progressao.lower() == 's':
				for i in range(N):
					termo = A1 + i * R
					stdscr.addstr(8 + i // num_digitos , i % num_digitos * (num_digitos + 3), f'{termo:^{num_digitos}}')
					if i < N - 1:
						stdscr.addch('>')
					else:
						stdscr.addch('.')
		elif opc == 2:
			loading_animation(stdscr)
			sleep(1)
			stdscr.clear()
			apresentacao(stdscr)
			N = 100
			AN = A1 + (N - 1) * R
			num_digitos = len(str(AN))
			stdscr.addstr(3, 0, f'》A{N} = {A1} + ({N} - 1) * {R}')
			stdscr.addstr(4, 0,f'》A{N} = {AN}')
			stdscr.addstr(6, 0,'Deseja ver a progressão completa [ S / N ]? ')
			mostrar_progressao = str(stdscr.getch(), 'utf-8')
			loading_animation(stdscr)
			if mostrar_progressao.lower() == 's':
				for i in range(N):
					termo = A1 + i * R
					stdscr.addstr(8 + i // num_digitos , i % num_digitos * (num_digitos + 3), f'{termo:^{num_digitos}}')
					if i < N - 1:
						stdscr.addch('>')
					else:
						stdscr.addch('.')
		elif opc == 3:
			loading_animation(stdscr)
			sleep(1)
			stdscr.clear()
			apresentacao(stdscr)
			N = 1000
			AN = A1 + (N - 1) * R
			num_digitos = len(str(AN))
			stdscr.addstr(3, 0, f'》A{N} = {A1} + ({N} - 1) * {R}')
			stdscr.addstr(4, 0,f'》A{N} = {AN}')
			stdscr.addstr(6, 0,'Deseja ver a progressão completa [ S / N ]? ')
			mostrar_progressao = str(stdscr.getch(), 'utf-8')
			loading_animation(stdscr)
			if mostrar_progressao.lower() == 's':
				for i in range(N):
					termo = A1 + i * R
					stdscr.addstr(8 + i // num_digitos , i % num_digitos * (num_digitos + 3), f'{termo:^{num_digitos}}')
					if i < N - 1:
						stdscr.addch('>')
					else:
					   stdscr.addch('.')
		elif opc == 4:
			loading_animation(stdscr)
			sleep(1)
			stdscr.clear()
			apresentacao(stdscr)
			AN = A1 + (N - 1) * R
			num_digitos = len(str(AN))
			stdscr.addstr(3, 0, f'》A{N} = {A1} + ({N} - 1) * {R}')
			stdscr.addstr(4, 0,f'》A{N} = {AN}')
			stdscr.addstr(6, 0,'Deseja ver a progressão completa [ S / N ]? ')
			mostrar_progressao = str(stdscr.getch(), 'utf-8')
			loading_animation(stdscr)
			if mostrar_progressao.lower() == 's':
				for i in range(N):
					termo = A1 + i * R
					stdscr.addstr(8 + i // num_digitos , i % num_digitos * (num_digitos + 3), f'{termo:^{num_digitos}}')
					if i < N - 1:
						stdscr.addch('>')
					else:
						stdscr.addch('.')
		elif opc == 5:
	            loading_animation(stdscr)
	            sleep(1)
	            stdscr.clear()
	            apresentacao(stdscr)
	            menu_opcoes = {
	                '1': 'Redefinir "N" (Ex: 189° posição)',
	                '2': 'Redefinir "R" (Ex: 356 em 356, 2 em 2...',
	                '3': 'Redefinir "A1" (início / começo / 1° número)'
	                }
	            for i, (opcao, descricao) in enumerate(menu_opcoes.items()):
	                stdscr.addstr(5 + i, 0, f'[{opcao}] - {descricao}')
	            stdscr.addstr(9, 0, 'Selecione uma opção: ')
	            opcoes = int(stdscr.getch()) - ord('0')
	            if opcoes == 1:
	                stdscr.addstr(11, 0, 'Redefina o valor de "N": ')
	                curses.echo()
	                N = int(stdscr.getstr())
	                curses.noecho()
	            if opcoes == 2:
	                stdscr.addstr(11, 0, 'Redefina o valor de "R": ')
	                curses.echo()
	                R = int(stdscr.getstr())
	                curses.noecho()
	            if opcoes == 3:
	                stdscr.addstr(11, 0, 'Redefina o valor de "A1": ')
	                curses.echo()
	                A1 = int(stdscr.getstr())
	                curses.noecho()
	            stdscr.clear()
	            apresentacao(stdscr)
	            AN = A1 + (N - 1) * R
	            num_digitos = len(str(AN))
	            stdscr.addstr(3, 0, f'》A{N} = {A1} + ({N} - 1) * {R}')
	            stdscr.addstr(4, 0,f'》A{N} = {AN}')
	            stdscr.addstr(6, 0,'Deseja ver a progressão completa [ S / N ]? ')
	            mostrar_progressao = str(stdscr.getch(), 'utf-8')
	            loading_animation(stdscr)
	            if mostrar_progressao.lower() == 's':
	                for i in range(N):
	                    termo = A1 + i * R
	                    stdscr.addstr(8 + i // num_digitos , i % num_digitos * (num_digitos + 3), f'{termo:^{num_digitos}}')
	                    if i < N - 1:
	                        stdscr.addch('>')
	                    else:
                        	stdscr.addch('.')
		elif opc == 6:
			finish_animation(stdscr)
			stdscr.addstr(22, 0,'Até mais!')
			break

def main():
	with ThreadPoolExecutor() as executor:
		future = executor.submit(calcular_PA)
		curses.wrapper(future.result)		

if __name__ == '__main__':
    main()
