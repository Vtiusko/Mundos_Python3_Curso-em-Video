def formula(n):
    # Declara uma lista para armazenar os termos já calculados
    termos = [0, 1]

    # Calcula os termos da sequência de Fibonacci
    for i in range(2, n + 1):
        termos.append(termos[i - 1] + termos[i - 2])

    # Retorna o termo solicitado
    return termos[n]


def menu():
    print("{:^40}\n".format("Sequncia Fibonacci"))
  
    # Declara uma lista para armazenar as opções
    opcoes = [("1", "Posição “N” do termo"), ("2", "Mostrar os 10 primeiros termos"), ("3", "Mostrar um período de termos"), ("4", "Sair do programa")]

    # Mostra as opções
    for opcao in opcoes:
        print(f"{opcao[0]} - {opcao[1]}")

    # Obtém a opção do usuário
    opcao = int(input("\nInforme a opção desejada: "))

    # Trata erros
    try:
        opcao = int(opcao)
    except ValueError:
        print("Opção inválida.")
        return

    # Executa a opção solicitada
    if opcao == 1:
        # Declara a variável enesimo como um inteiro
        enesimo = int(input("\nInforme a posição do termo: "))
        print(f"\nO termo de número {enesimo} é:\n>>> {formula(enesimo)}")

    elif opcao == 2:
        # Declara a variável comeca como um inteiro
        comeca = 0
        # Declara a variável termina como um inteiro
        termina = 9

        # Mostra sequencia de X à Y
        for i in range(comeca, termina + 1):
            print(f"Termo {i + 1}: {formula(i)}")
        
        pergunta_1 = input('\nDeseja calcular novamente [ S / N ]: ').upper().strip()
        
        while pergunta_1 == 'S':
        	lista_pergunta_2 = [
	        	('1', 'Incrementar posições'),
	        	('2', 'Decrementar posições'),
	        	('3', 'Voltar ao menu anterior'),
	        	('4', 'Finalizar o programa')
        	]
        
        
        	for alternativa in lista_pergunta_2:
        		print(f'{alternativa[0]} - {alternativa[1]}')
        
        	pergunta_2 = int(input('Informe a alternativa escolhida: ').strip().upper())
        	
        	if pergunta_2 == 'N':
        		break
        	
	        try:
	        	if pergunta_2 == 1:
	        		incrementa = int(input('Informe a quantidade a ser incrementada: '))
	        		termina += incrementa
	        		for i in range(comeca, termina +1):
	        			print(f'Termo {i+1} : {formula(i)}')
	        		
	        		pergunta_2 = int(input('Informe a alternativa escolhida: ').strip().upper())
        	
        			if pergunta_2 == 'N':
        				break   
	        					
	        	elif pergunta_2 == 2:
	        		decrementa = int(input('Informe a quantidade a ser decrementada: '))
	        		termina -= decrementa
	        		for i in range(comeca, termina +1):
	        			print(f'Termo {i+1} : {formula(i)}')
	        		
	        		pergunta_1 = input('\nDeseja calcular novamente [ S / N ]: ').upper().strip()
	        			
	        	elif pergunta_2 == 3:
	        		menu()
	        		
	        	elif pergunta_2 == 4:
	        		print('Até mais!')
	        		exit()
	        		
	        except ValueError:
	        	print('Informe um valor válido!')
	        	return
   

    elif opcao == 3:
        # Declara a variável comeca como um inteiro
        comeca = int(input("Informe o início da sequência: "))
        # Declara a variável termina como um inteiro
        termina = int(input("Informe o fim da sequência: "))

        # Mostra sequencia de X à Y
        for i in range(comeca, termina + 1):
            print(f"Termo {i + 1}: {formula(i)}")

        # Pergunta ao usuário o que deseja fazer
        opcao_seguir = input("O que deseja fazer? (I)niciar novamente, (A)umentar termos, (D)iminuir termos, (V)oltar ao menu, (S)air? ")

        while opcao_seguir not in ["I", "A", "D", "V", "S"]:
            opcao_seguir = input("Opção inválida. O que deseja fazer? (I)niciar novamente, (A)umentar termos, (D)iminuir termos, (V)oltar ao menu, (S)air? ")

        if opcao_seguir == "I":
            comeca = 0
            termina = 9
        elif opcao_seguir == "A":
            quant = int(input("Quantidade de termos a adicionar: "))
            termina += quant
        elif opcao_seguir == "D":
            quant = int(input("Quantidade de termos a remover: "))
            termina -= quant
        elif opcao_seguir == "V":
            menu()
        else:
            exit()

    else:
        exit()


# Inicia o programa
menu()
