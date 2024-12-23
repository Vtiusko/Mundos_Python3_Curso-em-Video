'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

	- ARARA
	- APOS A SOPA
	- SUBI NO ONIBUS
	- A SACADA DA CASA
	- O LOBO AMA O BOLO
	- A TORRE DA DERROTA
	- ANOTARAM A DATA DA MARATONA.

	
- FORMA ALTERNATIVA

frase = str(input('Digite uma frase/palavra,\npara verificar se é um palíndromo: ')).strip().upper()

palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]   <- AQUI QUE É DIFERENTE

if inverso == junto:
	print('	Temos um palíndromo!')
else:
	print('	Não temos um palíndromo!')
'''

frase = str(input('Digite uma frase/palavra,\npara verificar se é um palíndromo: ')).strip().upper()

# Vai fatiar pelos espaços
palavra = frase.split()

# Vai unir as palavras pelo o que está dentro das aspas
# No caso aqui, sem nada, sem espaços
junto = ''.join(palavra)

# Vai armazenar a frase ao contrário
inverso = ''

# Vai começar da última letra, para a primeira, de trás para frente
for letra in range(len(junto) -1, -1, -1):
	inverso += junto[letra]
print('\n- O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
	print('	Temos um palíndromo!')
else:
	print('	Não temos um palíndromo!')
