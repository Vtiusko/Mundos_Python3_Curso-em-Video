'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

	– IMC abaixo de 18,5: Abaixo do Peso
	– Entre 18,5 e 25: Peso Ideal
	– 25 até 30: Sobrepeso
	– 30 até 40: Obesidade
	– Acima de 40: Obesidade Mórbida

import os
.
.
.
os.system('clear') # limpa a tela

Você pode criar uma tabela usando a biblioteca `tabulate`, que torna fácil e rápida a criação de tabelas no console em Python. Aqui está um exemplo de como você pode usar o `tabulate` para criar uma tabela com as informações e valores do IMC.'''

from time import sleep
from tabulate import tabulate
from tqdm import tqdm

def calcular_imc(peso, altura):
	return peso / altura ** 2
	
imc_stats = [
    ('Subpeso Severo', '< 16'),
    ('Subpeso', '16 a 19,9'),
    ('Normal', '20 a 24,9'),
    ('Sobrepeso', '25 a 29,9'),
    ('Obeso', '30 a 39,9'),
    ('Obeso Mórbido', '> 40'),
]

status = [
	'Subpeso Severo',
	'Subpeso',
	'Normal',
	'Sobrepeso',
	'Obeso',
	'Obeso Mórbido'
]

print(f'{" ÍNDICE DE MASSA CORPORAL ":-^38}\n')
print(tabulate(imc_stats, headers=['SITUAÇÃO', 'IMC'], tablefmt='orgtbl'))
''' 
Para tabela, devemos informas os dados:
	- imc_stats	

O cabeçalho:
	- headers(aqui no caso será 'Situação' e 'IMC')

E após o formato da tabela:
	- tablefmt
'''
peso = float(input('\nDigite o peso (em kg): '))
altura = float(input('Digite a altura (em metros): '))

print('\n\nCARREGANDO...\n')
for i in tqdm(range(10), bar_format='{l_bar}{bar}|'):
	sleep(0.2)

imc = calcular_imc(peso, altura)
	
if imc < 16:	
	print(f'\nSeu IMC é {imc:.1f}',status[0])
elif imc < 19.9:
	print(f'\nSeu IMC é {imc:.1f}',status[1])
elif imc < 24.9:
	print(f'\nSeu IMC é {imc:.1f}',status[2])
elif imc < 29.9:
	print(f'\nSeu IMC é {imc:.1f}',status[3])
elif imc < 39.9:
	print(f'\nSeu IMC é {imc:.1f}',status[4])
else:
	print(f'\nSeu IMC é {imc:.1f}, se vai morrer logo logo!',status[5])


'''
Podemos otimizar a comparação utilizando um loop "for" para percorrer a lista de "imc_stats" e encontrar a faixa correspondente ao IMC calculado. Isso evita a repetição do código usando o "elif" para cada faixa.

Segue abaixo um exemplo de como fazer essa otimização:

```
for i in range(len(imc_stats)):
    if imc < float(imc_stats[i][1].split()[0]):
        print(f'\nSeu IMC é {imc:.1f}', imc_stats[i][0])
        break
    elif i == len(imc_stats) - 1:
        print(f'\nSeu IMC é {imc:.1f}', imc_stats[i][0])
```

Nesse código, percorremos a lista "imc_stats" com o loop "for", em que "i" é a posição atual na lista. Se o IMC estiver abaixo do intervalo da posição atual, imprimimos a classificação correspondente e saímos do loop com o "break". Se chegarmos à última posição da lista sem encontrar uma faixa que corresponda ao IMC, usamos o "elif" para imprimir a classificação correspondente.
'''










