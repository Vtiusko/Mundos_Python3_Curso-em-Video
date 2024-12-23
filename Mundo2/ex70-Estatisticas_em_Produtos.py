'''
Crie um programa que leie o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
    
    - Qual é o total gasto na compra
    - Quantos produtos custam mais de R$1.000
    - Qual é o nome do produto mais barato
'''

#from time import sleep
from os import name, system


def limpar():
    system('cls' if name == 'nt' else 'clear')
    

def mensagem():
    print('{0}\n{1:^40}\n{0}'.format('=' * 40, 'LOJÃO DEVcomprar'))


total = maior_que_mil = valor = cont = 0
mais_barato = ''

while True:
    limpar()
    mensagem()
    
    produto = input('Digite o nome do produto: ').capitalize().strip()
    preco = input(f'Informe o preço do {produto}: R$ ').strip()
    
    preco = float(preco)
    cont += 1
    total += preco

    # Verificando valores
    if preco > 1000:
        maior_que_mil += 1
    
    # Verifica qual o menor preço
    if cont == 1 or preco < valor:
        mais_barato = produto
        valor = preco
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [ S ] ou [ N ]: ')).strip().upper()[0]
    if resp == 'N':
        break


mensagem()
print('-> O total da compra foi de R${0:.2f}\n-> {2} item(s) custam mais que mil reais.\n-> {1} é o item mais barato.'.format(total, mais_barato, maior_que_mil))