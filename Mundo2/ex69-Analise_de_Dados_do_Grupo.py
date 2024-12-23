'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se a pessoa quer ou não continuar. Ao final mostre:
    
    - Quantas pessoas possuí mais de 18 anos.
    - Quantos homens foram cadastrados.
    - Quantas mulheres possuem menos de 20 anos.
'''

from os import system, name


def limpar():
    system('cls' if name == 'nt' else 'clear')
    

def cabecalho():
    print('{0}\n{1:^30}\n{0}'.format('=' * 30, 'ANÁLISE DE GRUPO'))


pessoas = []
man = maior_dezoito = mulher_menor_vinte = 0

while True:
    cabecalho()
    
    idade = input('Informe sua idade: ')
    sexo = input('Informe seu sexo [ M ] ou [ F ]: ').upper().strip()[0]
    
    pessoas.append([int(idade), sexo])
    
    parar = input('Deseja parar [ S ] ou [ N ]: ').upper()
    
    if parar == 'S':
        break
    
    limpar()

for pessoa in pessoas:
    idade = pessoa[0]
    sexo = pessoa[1]
    
    if sexo == 'M':
        man += 1
    elif idade > 18:
        maior_dezoito += 1
    elif (idade < 20) and (sexo == 'F'):
        mulher_menor_vinte += 1
    else:
         print('Algo deu errado!')

print(
    '\n{0}\n'
    'Homens cadastrados: {1}\n'\
    'Pessoas maiores de idade: {2}\n'\
    'Mulheres menores de 20 anos: {3}\n'\
    '{0}'.format(
        '=' *30, 
        man, 
        maior_dezoito, 
        mulher_menor_vinte
        )
    )