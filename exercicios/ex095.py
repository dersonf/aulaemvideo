#!/usr/bin/python3.6

'''
Exercício Python 095:
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

jogador = {}
partidas = []
cadastro = []
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    for p in range(1, int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))+1):
        partidas.append(int(input(f'Quantos gols na partida {p} foram marcados? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    cadastro.append(jogador.copy())
    while True:
        continua = str(input('Deseja adicionar mais jogadores? [S/N]? ')).upper().strip()[0]
        if continua in 'SN':
            break
        print('ERRO! Opção incorreta.', end = '')
    if continua == 'N':
        break
print('-=' * 30)
print(f'Cadastrado {len(cadastro)} jogadores')
print('-=' * 30)
print('id nome           gols                    total')
print('-=' * 30)
for c in range(0, len(cadastro)):
    print(f'{c:2} {cadastro[c]["nome"]:14} {str(cadastro[c]["gols"]):20} {cadastro[c]["total"]:>4}')
while True:
    detalhes = int(input('Exibir detalhes do jogador? [999 para sair] '))
    if detalhes == 999:
        break
    elif detalhes > len(cadastro) - 1:
        print(f'Jogador não cadastrado, tente de novo!!!')
    else:
        print(f'Detalhes do jogador {cadastro[detalhes]["nome"].upper()}')
        for c, v in enumerate(cadastro[detalhes]['gols']):
            print(f'No jogo {c+1} fez {v} gols')
