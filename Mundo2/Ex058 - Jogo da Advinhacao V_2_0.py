'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from tqdm import tqdm 
from random import randint
from time import sleep
from os import system, name


pc = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
	print('{:=^40}'.format(' JOGO DA ADVINHAÇAO '))
	player = int(input('\nAdvinhe o número de 0 - 10: '))
	palpites += 1
	print('')
	
	for i in tqdm(range(10), bar_format= '{l_bar}{bar}|'):
		sleep(0.01)
	
	if player == pc:
		acertou = True
	else:
		if player < pc:
			print('\nO número é maior, tente de novo!')
			sleep(2)
		if player > pc:
			print('\nO número é menor, tente mais uma vez!\n')
			sleep(2)
		system('cls' if name == 'nt' else 'clear')

print('\nParabéns!!! Acertou com {} chutes'.format(palpites))
