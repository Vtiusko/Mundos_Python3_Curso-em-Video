'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

from tabulate import tabulate
from os import system, name

p = []  
maior = 0  
menor = 0

for i in range(1, 6):
    print('{:=^40}'.format(f' {i} '))
    n = input('\n1 - Informe seu nome: ').title().strip()
    kg = float(input('2 - Informe seu peso (Kg): '))
    p.append([n, kg])
    system('cls' if name == 'nt' else 'clear')

if i == 1: #  Se i == 1 então ele será maior e menor
	maior = kg
	menor = kg
else:
	if kg > maior:
		maior = kg
# Se o kg for menor do que o menor peso...
	if kg < menor:
		menor = kg

# Por conta da float, tivemos que formatar a tabela
print(tabulate(p, headers=['NOME','PESO(KG)'], tablefmt='perona', floatfmt='0.3f'))

print('\n\nO MAIOR peso foi:\n{:.3f}'.format(maior))

print('\nO MENOR peso foi:\n{:.3f}'.format(menor))

'''
# import platform

# sistema = platform.system()
# print(f'O sistema operacional é: {sistema}')

	# system('cls' if name == 'nt' else 'clear')

	Essa linha de código verifica qual é o sistema operacional do computador antes de executar o comando para limpar a tela. Isso é importante porque o comando para limpar a tela é diferente dependendo do sistema operacional. Por exemplo, se o sistema operacional for Windows, o comando para limpar a tela é `'cls'`, mas se for outro sistema operacional, como Linux ou macOS, o comando é `'clear'`. A linha de código verifica qual é o sistema operacional usando a variável `name` e, em seguida, escolhe o comando apropriado para limpar a tela.
	
	Essa parte à princípio eu havia achado confusa, mas acabei entendendo um pouco, por isso vou deixar anotado. Temos a situação acima, para ver se o número é o maior ou o menor, primeiro devemos verificar quantas vezes ele se repete, por isso como base, utilizaremos o "i" (de iteração) do laço for. Ex:
		
		- Escolhemos um número apenas: "7"
		- O 7 se repetirá apenas uma vez.

	Qual é o número maior e qual é o menor? Isso mesmo! O número máximo e o mínimo é o 7.
'''
