'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

	– à vista dinheiro/cheque: 10% de desconto
	– à vista no cartão: 5% de desconto
	– em até 2x no cartão: preço formal 
	– 3x ou mais no cartão: 20% de juros
'''
from tabulate import tabulate
from os import system
from tqdm import tqdm
from time import sleep

forma_pgto = [
	('1', 'À vista dinheiro', '10%'),
	('2', 'À vista no cartão', '5%'),
	('3', 'Até 2x no cartão', 'preço normal'),
	('4', '3x ou mais no cartão', '20% de juros'),
]

carrinho = []

'''
quant = int(input('Informe a quantidade de itens: '))

 Adiciona itens ao carrinho
for i in range(quant):
	produto = str(input(f'\nInforme o {i+1}° protduto: ').title())
	quantidade = int(input('Quantidade: '))
	preço = float(input('Informe o preço: R$'))
	carrinho.append((produto, preço))
'''

print("Digite 'S' para finalizar o carrinho.")

while True:
    produto = input("\nInforme o produto: ").title().strip()
    # verifica se o usuário digitou 'Sair'
    if produto == 'S'.upper():
        break
    quantidade = int(input("Quantidade: "))
    preco = None

    # verifica se o usuário digitou um preço válido
    while preco is None:
        try:
            preco = float(input("Preço: R$ "))
        except ValueError:
            print("Preço inválido, tente novamente.")

    carrinho.append((produto, quantidade, preco))

#limpa a tela
system('clear')

'''
print(f"\n{len(carrinho)} itens adicionados ao carrinho:\n")

 imprime os itens do carrinho e calcula o total
total = 0

for produto, preco, quantidade in carrinho:
    valor_total = preco * quantidade
    total += valor_total
    print(f"{quantidade}x {produto} - R${preco:.2f} cada - total: R${valor_total:.2f}")

print(f"\nValor total do carrinho: R${total:.2f}")		
'''
			
print('\n')

# Acrescenta barra de progresso
for i in tqdm(range(10), bar_format='{l_bar}{bar}|'):
	sleep(0.23)

# limpa a tela
system('clear')

# Mostra os itens adicionados ao carrinho
print('\nOs seguintes itens foram adicionados ao carrinho!\n')
print(tabulate(carrinho, headers=['PRODUTOS','QUANTIDADE','PREÇO'], tablefmt='orgtbl'))
sleep(5)

print('\n')

# limpa a tela
system('clear')

# Calcula o valor total do carrinho
precos = 0

for item in carrinho:
	precos += item[1] * item[2]
		
# Opções de pagamento
print(tabulate(forma_pgto, headers=['OPÇÕES', 'FORMAS DE PAGAMENTO', 'DESCONTOS'], tablefmt='orgtbl'))

print(f'\n\nO valor da compra é de R${precos:.2f}\n')

# Mostra o tipo de pagamento
tipo_pgto = int(input('\nInforme o tipo de pagamento: '))	
if tipo_pgto == 1: # Opção 1
	pgto = precos - (precos * 10/100)	
	print(f'\nO valor total a ser pago é de: R${pgto:.2f}')
elif tipo_pgto == 2: # Opção 2
	pgto = precos - (precos * 5/100)
	print(f'\nO valor total a ser pago é de: R${pgto:.2f}')
elif tipo_pgto == 3: # Opção 3
	parc = int(input('\nOpções de parcelamento:\n1 - parcelar em 1X \n\n2 - parcelar em 2X vezes\n\nSelecione uma opção: '))
	while 1 != parc != 2:
		print('\nOpção Inválida!\n')
		parc = int(input('\nOpções de parcelamento:\n1 - parcelar em 1X \n\n2 - parcelar em 2X vezes\n\nSelecione uma opção: '))
	if parc == 1:
		print(f'\nO valor a ser pago é de: 1X de R${precos:.2f}')
	else:
		print('\nO valor total é de: R${:.2f}\nSerá pago em: 2X de R${:.2f}'.format(precos, precos / 2))
elif tipo_pgto == 4: # Opção 4
	vlr = precos + (precos * 20 / 100)
	parc = int(input('\nEm quantas vezes(acima de 2X): '))
	while True:
		parc = int(input('\nEm quantas vezes (acima de 2X): '))
		if parc <= 2:
			print('\nOpção inválida, escolha um número maior que 2.')
			continue
			break
	print('\nO valor total da compra é de: R${:.2f}.\nE será pago em: {}X de R${:.2f}'.format(precos, parc, vlr / parc))
