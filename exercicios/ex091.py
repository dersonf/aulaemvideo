#!/usr/bin/python36
from random import randint
from operator import itemgetter
dado = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = {}
print('Valores sorteados:')
for k, v in dado.items():
    print(f'O {k} tirou {v}.')
#ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
ranking = sorted(dado.items(), key=lambda x: x[1], reverse=True)
print('-=' * 20)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
