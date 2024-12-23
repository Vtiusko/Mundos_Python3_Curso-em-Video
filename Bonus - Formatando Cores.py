'''
Colocando cores no Python:

\033[0-7;30-37;40-47m O que eu quero aplicar a formatação / cor / fundo \033[m

* sempre separando por ';'

 ----- 0 - 9: Define o estilo da fonte; ------

0 = None (sem estilo)   4 = Underline (Sublinhado)
1 = Bold (Negrito)      7 = Negative (Inverte as cores)
2 = Fraco               8 = Oculta os Caracteres
3 = Itálico             9 = Tachado


----- 30 - 37: Define a cor da letra; -----

30 = Cinza      34 = Azul
31 = Vermelho   35 = Magenta
32 = Verde      36 = Ciano
33 = Amarelo    37 = Branco


----- 40 - 47: Define a cor de fundo; -----

40 = Fundo Cinza        44 = Fundo Azul
41 = Fundo Vermelho     45 = Fundo Magenta
42 = Fundo Verde        46 = Fundo Ciano
43 = Fundo Amarelo      47 = Fundo Branco
'''

print('\njo-ken-\033[01;33;41moooi\033[m!',end='\n\n')