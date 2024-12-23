'''
Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag.
'''
print('Digite "999" para parar.\n\n')

soma = quant = 0

while True:
    try:
        num = int(input('Informe um valor: '))
        
        if num == 999:
            break
    
        quant += 1
        soma += num
        
    except ValueError:
        print('\nVocê deve digitar um número!\n')

print(f'\n-> Foram digitados {quant} números')
print(f'-> A soma entre eles é: {soma}')
