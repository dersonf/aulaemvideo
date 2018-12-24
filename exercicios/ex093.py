#!/usr/bin/python3.6
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
for p in range(1, int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))+1):
    partidas.append(int(input(f'Quantos gols na partida {p} foram marcados? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partida(s)')
for c, v in enumerate(jogador['gols']):
    print(f' => Na partida {c+1} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gol(s).')

