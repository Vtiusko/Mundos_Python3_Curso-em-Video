'''
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

n = int(input('Digite qual a tabuada a ser exibida: '))

for i in range(0, 11):
	print('\33[32m{}\33[m x \33[32m{}\33[m = \33[32m{}\33[m' .format(n, i, n*i))
	