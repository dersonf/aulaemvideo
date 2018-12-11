#!/usr/bin/python36
ficha = []
cont = 'S'
while cont != 'N':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
print(f'ID - NOME            - MÉDIA')
print('='*30)
for c in range(0, len(ficha)):
    print(f'{c:<2} - {ficha[c][0]:15} - {ficha[c][2]:>4}')
print('='*30)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 exit)'))
    if aluno == 999:
        break
    else:
        for c, v in enumerate(ficha):
            if c == aluno:
                print(f'As notas de {ficha[c][0]} são {ficha[c][1]}')

