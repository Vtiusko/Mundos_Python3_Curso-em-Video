'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

	– Até 9 anos: MIRIM
	– Até 14 anos: INFANTIL
	– Até 19 anos: JÚNIOR
	– Até 25 anos: SÊNIOR
	– Acima de 25 anos: MASTER
'''

from datetime import date

print('''
O intuito deste programa é definir
a categoria de cada aluno para a CNN
ou Confederação Nacional de Natação, 
de acordo com a sua idade:
	
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
''')

# Uma lista vazia, para armazenar as informações
pessoas = []

# Aqui o usuário define o número de vezes que o loop repetirá
n_alunos = int(input('Digite a quantidade de alunos: '))

# E para chamar o número, atribuimos o vlr da variável dentro de range
for i in range(n_alunos):
	print('\n---------------------------------------')
	nom = str(input(f'Informe o nome do {i+1}° aluno(a): '))
	nasc = int(input('\nInforme o ano de nascimento: '))
	print('---------------------------------------')
	pessoas.append((nom, nasc))

atual = date.today().year	

#Definimos que nome e nascimento recebe o argumento pessoa
for pessoa in pessoas:
	nome, nasc = pessoa
	idade = atual - nasc
	print('--------------CATEGORIAS--------------\n')
	if 0 > idade <= 9:
		print(f'\n{nome}, voce tem {idade} anos, e sua categoria é MIRIM.')
	elif 10 > idade <= 14:
		print(f'\n{nome}, voce tem {idade} anos, e sua categoria é INFANTIL.')
	elif 15 > idade <= 19:
		print(f'\n{nome}, voce tem {idade} anos, e sua categoria é JÚNIOR.')
	elif 20 > idade <= 24:
		print(f'\n{nome}, voce tem {idade} anos, e sua categoria é SENIOR.')
	else:
		print(f'\n{nome}, voce tem {idade} anos, e sua categoria é MASTER.')

