#!/usr/bin/python36
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] <= 4:
    aluno['situacao'] = 'REPROVADO'
elif aluno['media'] <= 6.5:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'APROVADO'
print('-='*20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')

