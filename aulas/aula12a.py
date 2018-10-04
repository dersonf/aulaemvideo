#!/usr/bin/python36
nome = str(input('Qual é o seu nome? '))
if nome == 'Anderson':
    print('Nome bacana este, sua mãe tem excelente bom gosto!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Luciana':
    print('Seu nome é bem popular no Brasil')
else: # Opcional
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))
