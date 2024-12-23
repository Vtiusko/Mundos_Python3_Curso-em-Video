'''
Faça um programa que calcule a soma entre todos os números ÍMPARES que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

mult = []
soma = 0 # Soma todos os valores
cont = 0 # Conta a quantidade de itens

for i in range(1, 501, 2): # Números ímpares de 1 à 500
	if (i % 3) == 0:
		cont += 1
		soma += i
	mult.append((i)) # Adiciona os itens "i" à lista "mult"

print('A soma de todos os valores: {}\nA quantidade de itens: {}\n'.format(soma, cont))
print(mult)
