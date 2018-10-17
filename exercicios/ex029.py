#!/usr/bin/python36
v_max = 80
velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = float((velocidade - v_max) * 7.00)
    print('MULTADO! Você excedeu o limite permitido que é de {}Km/h'.format(v_max))
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

