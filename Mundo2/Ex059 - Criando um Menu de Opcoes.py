from tabulate import tabulate
from time import sleep
from os import system, name
from tqdm import tqdm

def limpar():
	for i in tqdm(range(10), bar_format='{l_bar}{bar}|'):
		sleep(0.1)
	system('cls' if name == 'nt' else 'clear')
	
def limpar2():
	sleep(3)
	system('cls' if name == 'nt' else 'clear')

def tabela():
	opcao = [
		['1',' Somar'],
		['2',' Multiplicar'],
		['3',' Maior'],
		['4',' Novos números'],
		['------', '----------------'],
		['5',' Sair do programa']
	]
	
	print(tabulate(opcao, headers=['OPÇÃO', 'DESCRIÇÃO'], tablefmt='orgtbl', stralign='left'))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

parar = False

while not parar:
	print('')
	tabela()
	escolha = int(input('\nInforme uma opção: '))

	if escolha == 1:
		soma = n1 + n2
		limpar()
		print('\nO resultado de {} + {} é: {}'.format(n1, n2, soma))
		limpar2()
	elif escolha == 2:
		produto = n1 * n2
		limpar()
		print('\nO resultado de {} x {} é: {}'.format(n1, n2, produto))
		limpar2()
	elif escolha == 3:
		limpar()
		if n1 > n2:
			print('\nO número {} é maior que {}.'.format(n1, n2))
		else:
			print('\nO número {} é maior que {}.'.format(n2, n1))
		limpar2()
	elif escolha == 4:
		limpar()
		tabela()
		n1 = int(input('\n\nDigite um valor: '))
		n2 = int(input('Digite outro valor: '))
		limpar2()
	elif escolha == 5:
		print('\nFINALIZANDO O PROGRAMA...')
		limpar()
		parar = True
	else:
		print('\nOpção inválida! Tente novamente...')
		limpar2()
