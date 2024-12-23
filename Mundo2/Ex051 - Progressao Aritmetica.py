'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

print('{:=^50}'.format(' Descobrir qual é a PA '))

p = int(input('\nPrimeiro termo: ')) # Primeiro termo
r = int(input('Razão: ')) # Razão
d = p + (10 - 1) * r # O enésimo(décimo) termo

print('')

for i in range(p, d + r, r):
	print('{} '.format(i), end='} ')
print('ACABOU')
