#!/usr/bin/python3.6

'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

pessoa = dict()
cadastro = list()
mulheres = idadetot = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            if pessoa['sexo'] == 'F':
                mulheres += 1
            break
        else:
            print('OPÇÃO INVÁLIDA!!!', end = '')
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    pessoa.clear()
    while True:
        cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if cont in 'SN':
            break
        else:
            print('OPÇÃO INVÁLIDA!!!', end = '')
    if cont == 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(cadastro)} pessoa(s).')
for c in range(0, len(cadastro)):
    idadetot += cadastro[c]['idade']
media = idadetot / len(cadastro)
print(f'A média de idade é {idadetot / len(cadastro)}.')
if mulheres > 0:
    print(f'As mulheres são:')
    for c in cadastro:
        if c['sexo'] == 'F':
            print(f' => {c["nome"]}')
print('As pessoas com idade superior a média são:')
for c in cadastro:
        if c['idade'] > media:
            print(f'  ==> {c["nome"]} do sexo {c["sexo"]} possui {c["idade"]} anos.')
