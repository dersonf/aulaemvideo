#!/usr/bin/python36
import random
vitoria = 0
print('-'*30)
print('A brincadeira só acaba quando o computador vencer.')
print('-'*30)
while True:
    jogador = int(input('Quantos dedinhos: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar: [P/I] ')).upper().strip()[0]
    computador = int(random.randint(1,10))
    soma = jogador+computador
    resultado = soma % 2
    if resultado == 0:
        parimpar = 'PAR'
    else:
        parimpar = 'IMPAR'
    if resultado == 0 and escolha == 'P' or resultado != 0 and escolha == 'I':
        print(f'You win!!! Computador escolheu {computador} e você {jogador}, o total foi {soma}, deu {parimpar}')
        vitoria += 1
    else:
        break
print(f'You loose!!! O computador escolheu {computador} e você {jogador}, {soma} é {parimpar}!!!\nQuantidade de vitória(s) consecutivas foi {vitoria}.\n\033[1;31;44mFIM DE JOGO\033[m.')
