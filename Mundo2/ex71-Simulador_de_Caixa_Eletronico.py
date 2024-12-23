'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

# Ex 71 - Simulador de Caixa Eletrônico

cedulas = [50, 20, 10, 1]

while True:
    try:
        valor = input('Informe o valor a ser sacado: R$').strip()

        print('\n')

        saque = int(valor)


        for cedula in cedulas:
            # Calcula quantidades de cédulas
            quant_cedula = saque / cedula

            # Pega a quantidade de cédula e multiplica para tirar a diferença do valor de saque
            saque = saque - (int(quant_cedula) * cedula)
        
            print(f'Foram sacadas {int(quant_cedula)} cédulas de {cedula}')

        print(f'\nTotalizando R${int(valor):.2f}')

    except ValueError as erro:
                print(f'ERRO: {erro}')