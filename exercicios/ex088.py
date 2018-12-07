#!/usr/bin/python36
from random import sample
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
jogos = int(input('Quantos jogos você quer que sorteie? '))
print('-=' * 3, f' Sortenado {jogos} JOGOS ', '-=' * 3)
for c in range(1, jogos+1):
    numeros = sorted(sample(range(1, 60), k=6))
    print(f'Jogo {c}: {numeros}')

