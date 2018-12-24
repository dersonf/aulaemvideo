#!/usr/bin/python36
pessoa = dict()
cadastro = list()
mulheres = idadetot = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            if sexo == 'F':
                mulheres += 1
            break
        else:
            print('OPÇÃO INVÁLIDA!!!')
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    pessoa.clear()
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(cadastro)} pessoa(s).')
for c in range(0, len(cadastro)):
    idadetot += cadastro[c]['idade']
print(f'A média de idade é {idadetot / len(cadastro)}.')
if mulheres > 0:
    print(f'As mulheres são:')
    for c in cadastro:
        if c['sexo'] == 'F':
            print(f' => {c["nome"]}')

