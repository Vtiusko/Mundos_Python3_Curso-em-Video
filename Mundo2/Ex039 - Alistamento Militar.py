'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

SITE REFERENCIA:
	https://vaiprogramar.com/como-trabalhar-com-data-hora-python-datetime/
	
import calendar

nasc = int(input('\nInforme o ano do seu nascimento: '))#1
mes = int(input('\nInforme o mês: ')) #2
print('\n\n----------CALENDÁRIO----------')

if mes >= 1 and mes <= 12: #3
	cal = calendar.month(nasc, mes) #4
	print('\nEsse é o Calendário do mês', mes)
	print('\n--------------------------------\n') #5
	print(cal) #6
	print('\n--------------------------------') #7
else:
	print('\nEntrada inválida')

Pra definir se idade for menor que 18, podemos fazer uma
subtração de 18 - idade. E se já passou, idade - 18.
'''
from datetime import date

sexo = str(input('Informe seu sexo [ M / F ]: ').upper())

def alistamento():
	nasc = int(input('\nInforme o ano do seu nascimento: '))
	ano_atual = date.today().year
	idade = ano_atual - nasc

	if idade == 18:
		print('\nAeeee {} anos... Chegou a hora de carpir mato!'.format(idade))
	elif idade < 18:
		ano = ano_atual - (idade - 18)
		print('\n{} anos? Está chegando hein, se prepare, faltam {} ano(s)\nSeu alistamento será em {}'.format(idade, 18 - idade, ano))
	elif idade > 18:
		ano = ano_atual - (idade - 18)
		print('\n{} anos, boa guerreiro,\npassaram {} ano(s) do seu alistamento.\nSe não se alistou ainda, faz o favor né!\nSeu alistamento foi em {}'.format(idade, idade - 18, ano))
	
if sexo == 'M':
	alistamento()
else:
	print('\nMulher, tem obrigatoriedade no alistamento!')
	