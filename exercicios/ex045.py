#!/usr/bin/python36
from random import randint
import sys
itens = ('Pedra', 'Pepal', 'Tesoura')
print('''--- JOKENPÔ ---
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador > 2:
    print('Opção inválida, acabou a brincadeira.')
    sys.exit()
computador = randint(0 ,2)
if jogador == computador:
    print('EMPATOU, você colocou {} e o computador {}.'.format(itens[jogador], itens[computador]))
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('VOCÊ VENCEU, você escolheu {} e o computador {}.'.format(itens[jogador], itens[computador]))
else:
    print('COMPUTADOR VENCEU, você escolheu {} e o computador {}.'.format(itens[jogador], itens[computador]))

