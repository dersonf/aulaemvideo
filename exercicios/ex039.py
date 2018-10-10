#!/usr/bin/python36
from datetime import date
ano = int(input('Ano de nascimento: '))
idade_alistamento = 18
ano_alistamento = ano + idade_alistamento
agora = date.today().year
idade = agora - ano
print('Você está com {} anos.'.format(idade))
print('Você deve se alistar em {}.'.format(ano_alistamento))
if agora == ano_alistamento:
    print('Você deve se alistar IMEDIATAMENTE.')
elif agora > ano_alistamento:
    print('Você deveria ter se alistado há {} ano(s).'.format(agora - ano_alistamento))
else:
    print('Ainda é cedo, deve se alistar em {} ano(s).'.format(ano_alistamento - agora))
