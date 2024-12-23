'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

def boas_vindas():
    print('{:=^40}'.format(' LEITOR DE NÚMEROS '))
    
    print('{:>40}\n\n{:40}'.format(' NOTA AO USUÁRIO ', 'Digite quantos números desejar\no programa analisará:\n\n-> Qual é o maior e o menor;\n-> Qual a média entre eles;\n\nPressione "P" para parar o programa\nBoa interatividade!'))

def maior_e_menor(n):
    return max(n), min(n)

def calc_media(n, contador):
    soma = sum(n)

    media = soma / contador

    return media

def execucao(n):
    num = n.split()
    valores = []
    contador = 0

    for n in num:
        valores.append(int(n))
        contador += 1

    maximo, minimo = maior_e_menor(valores)
    media = calc_media(valores, contador)

    return media, maximo, minimo, valores, contador



boas_vindas()
print('')
while True:
    try:
        num = input('Digite quantos números você quiser: ').upper()
        if str(num) == 'P':
            maximo, minimo = maior_e_menor(num)
            _, _, _, _, contador = execucao(num)

            print('\n\nForam digitado(s): {}'.format(contador))
            print('O menor número é o: {}'.format(minimo))
            print('O maior número é o: {}'.format(maximo))
            print('\nAté mais!\n\n')
            break
        elif int(num) != 'P':
            media, maximo, minimo, valores, contador = execucao(num)
    except ValueError:
        print('\nValor inválido,\ntente novamente!\n')0