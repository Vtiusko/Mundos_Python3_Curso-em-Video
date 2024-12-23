from time import sleep
from tqdm import tqdm

'''
Desenvolva um programa que leia as notas de um aluno, calcule e mostre a sua média.
'''
print('\033[1;33m----------CÁLCULO DE MÉDIA ESCOLAR----------\033[m\n')

def calculo_escolar():
	sleep(1)
	n1 = float(input('\n\033[1;33m1)\033[m Digite sua nota do \033[1;33m1°\033[m semestre:\033[1;32m '))
	n2 = float(input('\033[m\033[1;33m2)\033[m Digite sua nota do \033[1;33m2°\033[m semestre:\033[1;32m '))
	n3 = float(input('\033[m\033[1;33m3)\033[m Digite sua nota do \033[1;33m3°\033[m semestre:\033[1;32m '))
	n4 = float(input('\033[m\033[1;33m4)\033[m Digite sua nota do \033[1;33m4°\033[m semestre:\033[1;32m '))
	s = (n1 + n2 + n3 + n4) / 4
	print('\033[m\n\n\033[1;33mCalculando...\033[m\n')

	for i in tqdm(range(10)):
		sleep(0.2)

# pode fazer assim tbm "if 2.9 > s >= 0:"		
	if s >= 0 and s <= 2.9:
		print(f'\nSua nota foi: \033[1;4;31m{s:.1f}\033[m \033[1;4;31m(Péssimo)\033[m, as aulas foram realmente assistidas??\n') 
	elif s >= 3 and s <= 4.9:
		print(f'\nSua nota foi: \033[1;4;35m{s:.1f}\033[m \033[1;4;35m(Ruim)\033[m, voce tem que estudar mais!\n')
	elif s >= 5 and s <= 5.9:
		print(f'\nSua nota foi: \033[1;4;33m{s:.1f}\033[m \033[1;4;33m(Regular)\033[m, passou raspando, hein!\n')
	elif s >= 6 and s <= 8.9:
		print(f'\nSua nota foi: \033[1;4m{s:.1f}\033[m \033[1;4m(Bom)\033[m, voce passou!\n')
	elif s >= 9 and s <= 10:
		print(f'\nSua nota foi: \033[1;4;32m{s:.1f}\033[m\033[1;4;32m(Excelente)\033[m, seus esforços valeram a pena, parabéns!!!\n')
		
while True:
    calculo_escolar()
    # Capturando e avaliando a resposta.
    resp = input('\nDeseja continuar? \033[1;33m[ S / N ]\033[m ').upper()
    while (len(resp) != 1) or (resp not in 'SN'):
        print('\n\033[1;31mDigite apenas\033[m \033[1;33m"S"\033[m \033[1;31mou\033[m \033[1;33m"N"\033[m!\n')
        resp = input('\n\nDeseja continuar? \033[1;33m[ S / N ]\033[m ').upper()
    if resp == 'N':
        break
	