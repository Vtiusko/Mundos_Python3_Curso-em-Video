'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

num = []
soma = 0
cont = 0

for i in range(1, 7):
	n = int(input(f'Digite o {i}° número inteiro: '))
	if n % 2 == 0:
		soma += n # Soma o valor total
		cont += 1 # Soma a quantidade de itens
		num.append((n)) # Adiciona o item "n" à lista "num"

print('\n- Quantidade de números pares: {}\n- Números pares: {}\n- Total dos valores pares: {}'.format(cont, num, soma))
