'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usiário. O programa será interrompido quando o número solicitado for negativo.
'''
from time import sleep
from os import system, name


def limpar():
    system('cls' if name == 'nt' else 'clear')


while True:
    try:
        print('{0}\n{1:^35}\n{0}'.format('=' * 35, 'CRIADOR DE TABUADA'))
        num = int(input('Informe um número: '))
        print('=' * 35)
        
        if num < 0:
            print('\nAté mais!')
            break
            
        for n in range(10):
            print(f'{num} x {n + 1} = {num * (n + 1)}')
        
        print('=' * 35)
        sleep(3)
        limpar()
    
    except ValueError:
        print('\nVocê deve digitar um número!')
        sleep(2)
        limpar()