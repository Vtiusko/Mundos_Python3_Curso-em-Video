'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

print('{:=^40}'.format(' CONTADOR DE DÍGITOS '))
print('{:^40}'.format(' - digite 999 para finalizar - '),end='\n\n')

num = soma = contador = 0
media = None

while True:
    num = input('Digite o valor: ')
    try:
        num = int(num)
        
        if num == 999:
            break

        elif num >= 0 and num <= 998:
            contador += 1
            soma += num

        elif num < 0 or num > 999:
            print('\nValor inválido,\ntente novamente!\n')

    except ValueError:
        print('\nValor inválido,\ntente novamente!\n')

if contador > 0:
    media = soma / contador

print(f'\nForam digitados: {contador} número(s)')
print(f'A soma entre eles é de: {soma}')
if media is not None:
    print(f'A média de valores é igual à: {media:.2f}')
else:
    print('\nNenhum número válido foi digitado,\nentão a quantidad, some e emédia não puderam ser calculados.')