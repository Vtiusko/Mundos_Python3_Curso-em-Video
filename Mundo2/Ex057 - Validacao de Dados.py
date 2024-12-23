'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

nome = str(input('Informe seu nome: ')).title().strip()
genero = str(input('\nInforme seu Sexo [M/F]: ')).upper().strip()

while genero not in 'MF':
	print('\nValor inválido! Digite o valor correto!')
	genero = str(input('\nInforme seu Sexo [ M / F ]: ')).upper().strip()
	
if genero == 'M':
	genero = 'HOMEM'
if genero == 'F':
	genero = 'MULHER'
	
print('\nPrazer em conhece-lo {}!\nVejo aqui que voce é {}!'.format(nome, genero))
