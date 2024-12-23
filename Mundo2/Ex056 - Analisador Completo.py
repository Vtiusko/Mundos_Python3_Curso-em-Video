'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
from datetime import date
from os import system, name
from tabulate import tabulate
from tqdm import tqdm
from emoji import emojize
from time import sleep

pessoas = [] # Armazena as pessoas
nome_homem_mais_velho = '' # Armazena o nome do homem mais velho
idade_homem_mais_velho = 0 # Armazena idade homem mais velho
mulheres_novas = [] # Armazena as mulheres menores de 20 anos
qtd_mulheres_novas = 0 # Armazena a quantidade de mulheres < 20 anos
soma_idade = 0 # Armazena a soma das idades

n = int(input('Quantas pessoas serão verificadas: '))
system('cls' if name == 'nt' else 'clear')

for i in range(1, n + 1):
    print('{:=^35}'.format(f' {i}ª PESSOA '))
    nome = input('\n1 - Seu nome: ').title().strip()
    nasc = int(input('2 - Ano de nascimento: '))
    genero = input('3 - Sexo [ M / F ]: ').strip().upper()
    system('cls' if name == 'nt' else 'clear')
    idade = date.today().year - nasc
    soma_idade += idade
    pessoas.append([nome, idade, genero])
    
# Verifica quem é o homem mais velho  
if i == 1 and genero == 'M':
	idade_homem_mais_velho = idade
	nome_homem_mais_velho = nome
else:
	if genero == 'M' and idade > idade_homem_mais_velho:
		idade_homem_mais_velho = idade
		nome_homem_mais_velho = nome
if genero == 'F' and idade < 20:
	mulheres_novas.append([nome, idade])
	qtd_mulheres_novas += 1

media = soma_idade / n

for i in tqdm(range(10), desc='PROCESSANDO...', bar_format='{desc}{bar}'):
    sleep(0.3)
    
system('cls' if name == 'nt' else 'clear')

# Define os tipos de mulheres do grupo.
'''
	O método `Join` espera uma lista iterável de strings, ao utilizá-lo em uma lista com vários tipos de valores (uma lista contendo tuudo junto valores: bool, int, float,str), será necessário extrair o tipo de valor que queremos, armazená-lo à uma variàvel, e por fim, utilizar o método `join`.
	Como no código abaixo:
		
		Extração: ```nomes = [item[0] for item in mulheres_novas]```
		Utilização do método: ```print(*intruões*', ' '.join(nomes))```
'''
if qtd_mulheres_novas == 0:
	def x():
		print(emojize(f'\n:baby:', use_aliases=True), end='')
		print(f' - \033[33mulheres_novasENHUMA\033[m mulher tem menos de 20 anos.')
elif qtd_mulheres_novas == 1:
	def x():
		nomes = [item[0] for item in mulheres_novas]
		print(emojize(f'\n:baby:', use_aliases=True), end='')
		print(f' - \033[33m{qtd_mulheres_novas}\033[m mulher tem menos de 20 anos.\n- ', ', '.join(nomes))
else:
	def x():
		nomes = [item[0] for item in mulheres_novas]
		print(emojize(f'\n:baby:', use_aliases=True), end='')
		print(f' - \033[33m{qtd_mulheres_novas}\033[m mulheres tem menos de 20 anos:\n- ', ', '.join(nomes))

print(tabulate(pessoas, headers=['NOME', 'IDADE', 'GENERO'], tablefmt='orgtbl')) # Tabela com o grupo.

x() # Mostra os tipos de mulher do grupo.

# Mostra o homem mais velho do grupo.
print(emojize(f'\n:old_man:', use_aliases=True), end='')
print(f' - O nome do homem mais velho é\033[33m{nome_homem_mais_velho}\033[m com \033[33m{idade_homem_mais_velho}\033[m anos.')

# Mostra a média de idade do grupo.
print(emojize(f'\n:hourglass_not_done:', use_aliases=True), end='')
print(f' - A média de idades do grupo é de \033[33m{media:.1f}\033[m anos.') 

'''
A função `join` é um método de string em Python que recebe um iterável (como uma lista ou uma tupla) como argumento e retorna uma string que é a concatenação de todos os elementos do iterável, separados por um separador especificado.

Por exemplo, suponha que você tenha a seguinte lista de strings:

------- python -------
my_list = ['apple', 'banana', 'cherry']

Você pode usar a função `join` para criar uma única string com todos os elementos da lista, separados por um espaço:

------- python -------
my_string = ' '.join(my_list)
print(my_string)

Isso imprimirá a seguinte string:

	- apple banana cherry

Você pode alterar o separador passando um caractere diferente para a função `join`. Por exemplo, para separar os elementos com vírgulas, você pode fazer o seguinte:

------- python -------
my_string = ', '.join(my_list)
print(my_string)

Isso imprimirá a seguinte string:

	- apple, banana, cherry
'''