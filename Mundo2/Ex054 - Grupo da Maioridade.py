'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from tqdm import tqdm
from os import system
from tabulate import tabulate
from datetime import date
from time import sleep

n = int(input('Informe a quantidade de pessoas a ser\nanalisadas a maioridade: '))
system('clear')

lista = []
maioridade = []
menoridade = []
maior = 0
menor = 0

for i in range(1, n+1):
	nome = input(f'{i} - Informe seu nome: ').title()
	nasc = int(input('Informe seu ano de nascimento: '))
	idade = date.today().year - nasc
	lista.append([nome, idade])
	
	if idade >= 18:
		maioridade.append([nome, idade])
		maior += 1
	else:
		menoridade.append([nome, idade])
		menor += 1
		
	system('clear')

system('clear')

print('CARREGANDO...')
for i in tqdm(range(10), bar_format='{l_bar}{bar}|'):
	sleep(0.2)

system('clear')

print(tabulate(lista, headers=['NOME', 'IDADE'], tablefmt='presto'))

sleep(10)

system('clear')

print('As pessoas MAIORES de idade são:\n{}\n\nQuantidade: {}'.format(tabulate(maioridade, headers=['NOME', 'IDADE'], tablefmt='presto'), maior))

print('\n\nAs pessoas MENORES de idade são:\n{}\n\nQuantidade: {}'.format(tabulate(menoridade, headers=['NOME', 'IDADE'], tablefmt='presto'), menor))
