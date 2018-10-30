#!/usr/bin/python36
import random
import time
tentativas = 1
computador = int(random.randint(0, 10))
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
while computador != jogador:
    tentativas += 1
    jogador = int(input('ERROUU!!! Tente de novo. '))
print('PROCESSANDO...')
time.sleep(3)
if tentativas == 0:
    print('Acertou de primeira, parabéns!!!')
else:
    print('Você acertou depois de {} tentativas.'.format(tentativas))

