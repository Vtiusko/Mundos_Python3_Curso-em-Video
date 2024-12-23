#pylint:disable=E0401
'''
Faça o computador jogar JOKENPO com voce.
'''

from os import system
from time import sleep
from emoji import emojize
from random import randint

# -------------- Apresentação do GAME 
def apresentacao():
	print('{:=^50}'.format(' Bora jogar JO-KEN-PO comigo? '))

# ---------------------- Nome jogador
apresentacao()
opc1 = emojize(':fist:')
opc2 = emojize(':raised_hand:')
opc3 = emojize(':victory_hand:')

name = str(input('\nInforme o seu nome: '))
print(f'\nOlá {name}, vamos jogar JO-KEN-PO!')
sleep(2)
system('clear')

apresentacao()

# ----------------- Emoji das jogadas
print('\nOpções para escolher:\n')
print(f'[1] {opc1}\n')
print(f'[2] {opc2}\n')
print(f'[3] {opc3}\n')

opc = int(input('Escolha uma opção: '))
system('clear')

#  ------ Gera item aleatório para PC
itens = [
	opc1,
	opc2,
	opc3
]

aleatorio = randint(0, 2)
PC = itens[aleatorio]

#  ---- Gera item aleatório para USER
USER = ''

if opc == 1:
	USER = opc1
elif opc == 2:
	USER = opc2
elif opc == 3:
	USER = opc3
else:
	print('\nVálor Inválido!')
	opc = int(input('\nEscolha uma opção: '))
	print(f'[1] {opc1}\n')
	print(f'[2] {opc2}\n')
	print(f'[3] {opc3}\n')

print('\nJO-',end='')
sleep(1)
print('KEN-',end='')
sleep(1)
print('PO!!!')

# ------------------- Lógica da coisa
if USER == PC:
    print('\n{} vs {}!\n\n\033[33m- EMPATE TÉCNICO!\033[m'.format(USER, PC))
elif (USER == 1 and PC == 3) or \
     (USER == 2 and PC == 1) or \
     (USER == 3 and PC == 2):
    print('\n\n{} vs {}!\n\n- \033[32mVOCÊ ganhou!\033[m'.format(USER, PC))
else:
    print('\n\n{} vs {}!\n\n\033[31m- O COMPUTADOR ganhou!\033[m'.format(USER, PC))
