'''
Faça um programa que jogue par ou ímpar com o seu computador. O programa será interrompido quando o jogador perder. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


Por que a probabilidade é de 50%?

Considere todas as combinações possíveis de dedos que os jogadores podem mostrar:

Par + Par: Soma par, vitória do jogador "par".
Par + Ímpar: Soma ímpar, vitória do jogador "ímpar".
Ímpar + Par: Soma ímpar, vitória do jogador "ímpar".
Ímpar + Ímpar: Soma par, vitória do jogador "par".


_*Lógica do Jogo:*_

1 - PAR
2 - IMPAR

se eu escolher par e o pc impar ele ganha
se eu escolher impar e o pc tbm ele ganha
se eu escolher par e o pc tbm, eu ganho
se eu escolher impar e o pc par eu ganho
'''

from random import randint
from os import name, system
from time import sleep


def limpar():
    system('cls' if name == 'nt' else 'clear')


def mensagem(n):
    print('{1}\n{0:^36}\n{1}'.format('===== Vamos jogar ÍMPAR ou PAR =====', '-' * 36))
    print(f'Vitórias consecutivas: {n}')


vitorias = 0

while True:
    mensagem(vitorias)
    
    print('\nDentre as opções...\n\nP -> PAR\nI -> ÍMPAR\n')
    
    # Número aleatório do computador
    pc = randint(0, 10)
    
    # Escolhas do jogador
    escolha = input('Escolha [ P / I ]: ').upper().strip()
    num_jogador = int(input('Digite um número: '))
    
    # Soma os números do pc e jogador
    soma = pc + num_jogador
    total = 'P' if soma % 2 == 0 else 'I'
    
    # Limpa a tela e mostra a função memsagem
    limpar()
    mensagem(vitorias)
    
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    
    # Mostra os números escolhidos, 
    # total e resultado Par ou Ímpar
    print(f'\n-> Jogador: {num_jogador}\n-> Computador: {pc}\n\nO resultado foi: {soma}. Deu {resultado}')
    print('-' * 36)
    
    # Se o jogador ganhar, adicione +1 na vitória
    if escolha == total:
        print('Você ganhou. Parabéns!')
        vitorias += 1
        sleep(5)
        
        
    elif escolha != total:
        print('O computador ganhou dessa vez!\n\nVOCÊ PERDEU!')
        sleep(5)
        break
    
    
    limpar()

