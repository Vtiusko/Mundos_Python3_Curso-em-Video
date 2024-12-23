'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep
from os import system
from emoji import emojize


print('A contagem regressiva vai iniciar...\n\n')
sleep(3)
system('cls')

for i in range(10, -1, -1):
	print(i)
	sleep(1)
	system('cls')
print(emojize('FELIZ ANO NOVO!!! :fireworks:'))
