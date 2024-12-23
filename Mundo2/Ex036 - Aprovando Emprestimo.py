'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
from tqdm import tqdm
from time import sleep


print('\033[4;1;7;30;47m=====  LIMITE RÁPIDO E NA HORA! (para imóvel)  =====\033[m')

casa = float(input('\nDigite o valor desejado do \033[4;1;32mempréstimo\033[m: R$\033[1;32m')) #Valor do imóvel
salario = float(input('\033[m\nInforme seu salário: R$\033[1;32m')) #Salário
limite = salario * 0.3
tipo_parcelas = int(input('\033[m\nComo será pago: \n\n\033[1;33m1 -\033[m Parcelas de até \033[1;33m12X\033[m\n\033[1;33m2 -\033[m Parcelas à partir de \033[1;33m1 ano\033[m\n\nEscolha uma opção: \033[1;33m')) #Parcelas


if tipo_parcelas == 1:
	n_parc = int(input('\033[m\nQuantidade de parcelas ate \033[1;33m12X\033[m: \033[1;33m'))
	mes = casa / n_parc
	print('\n\033[32mCALCULANDO EMPRÉSTIMO...\033[m\n')
	for i in tqdm(range(10)):
		sleep(0.2)	
	if mes > limite:
		print('\n\033[1;31mEmpréstimo Negado\033[m!!! Parcela no valor de \033[1;32mR${:.2f}\033[m, excede \033[4m30%\033[m do salário.'.format(mes))
	else:
		print('\nO imóvel no valor de \033[1;32m{:.2f}\033[m, será pago em \033[1;33m{}X\033[m de \033[1;32mR${:.2f}\033[m'.format(casa, n_parc, mes))
elif tipo_parcelas == 2:
	n_anos = int(input('\033[m\nDigite a quantidade de anos: \033[1;33m'))
	ano = casa / (n_anos * 12)
	print('\n\033[32mCALCULANDO EMPRÉSTIMO...\033[m\n')
	for i in tqdm(range(10)):
		sleep(0.2)	
	if ano > limite:
		print('\n\033[1;31mEmpréstimo Negado\033[m!!! Parcela no valor de \033m[1;32R${:.2f}\033[m, excede \033[4m30%\033[m do salário.'.format(ano))
	else:
		print('\nO imóvel no valor de \033[1;32m{:.2f}\033[m, será pago em \033[1;33m{}X\033[m de \033[1;32mR${:.2f}\033[m'.format(casa, n_anos*12, ano))
