'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. E mostrar que tipo de triângulo será formado:

	– EQUILÁTERO: todos os lados iguais
	– ISÓSCELES: dois lados iguais, um diferente
	– ESCALENO: todos os lados diferentes
'''
from time import sleep
from emoji import emojize
from tqdm import tqdm

print(emojize('Verifique se as suas retas \033[37mPODEM\033[m ou \033[37mNÃO\033[m formar um triangulo\nSiga os passos abaixo:selfie:'))

'''
Para mostrar apenas a barra de progresso, sem as informações ao lado, você pode definir o parâmetro `bar_format` na criação do objeto tqdm. Por exemplo:

```CÓDIGO```
from tqdm import tqdm
from time import sleep

for i in tqdm(range(10), bar_format='{l_bar}{bar}|'):
    sleep(0.3)
`````````````
    
No parâmetro `bar_format` utilizado em um objeto da classe tqdm, a string `'|'` adicionada no final representa um separador que aparece após a barra de progresso, marcando o final da mesma.

A string `{l_bar}` representa o conteúdo à esquerda da barra de progresso, enquanto `{bar}` representa a própria barra de progresso. Então, juntando-se essas duas strings com um `'|'` no final, teremos a seguinte disposição:

```
Conteúdo à esquerda da barra de progresso      Barra de progresso   |
```

Assim, o separador `'|'` é adicionado apenas como um enfeite visual para indicar que a barra não continua infinitamente à direita da tela. Mas é importante ressaltar que o que vem após a barra de progresso é determinado única e exclusivamente pelo `'|'` em si, ou seja, poderia ser qualquer outra string que você desejasse. Por exemplo:

```
bar_format='{l_bar}{bar} - Concluído!'
``` 

Nesse caso, a barra de progresso seria acompanhada pela string " - Concluído!" após a barra de progresso indicar o término do processo em execução..
'''

print('\n\n\033[32mCarregando...\033[m\n')
for i in tqdm(range(10), bar_format='{l_bar}{bar}|'):
    sleep(0.3)

r1 = float(input('\n\nDigite o valor do primeiro angulo: '))
r2 = float(input('\nDigite o valor do segundo angulo: '))
r3 = float(input('\nDigite o valor do terceiro angulo: '))


if r1 + r2 > r3 and r3 + r1 > r2 and r3 + r2 > r1:
	tri = ''
	if r1 == r2 == r3:
		tri = 'TRIANGULO EQUILÁTERO'
	elif r1 == r2 != r3 or r2 == r3 != r1:
		tri = 'TRIANGULO ISÓSCELES'
	elif r1 != r2 != r3:
		tri = 'TRIANGULO ESCALENO'
	print('\nSuas medidas {}, {}, {},\n\033[37mPODEM\033[m formar um triangulo, sendo ele um {}!'.format(r1, r2, r3, tri))
else:
	print('\nSuas medidas {}, {}, {},\n\033[31mNÃO PODEM\033[m formar um triangulo'.format(r1, r2, r3))




