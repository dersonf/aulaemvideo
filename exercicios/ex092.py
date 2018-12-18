#!/usr/bin/python36
from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Nº da carteira de Trabalho [0 não tem]'))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
pessoa['aposentadoria'] = (pessoa['idade'] +
    (35 - (date.today().year - pessoa['contratação'])))
print('-=' * 30)
for k,v in pessoa.items():
    print(f' - {k} tem valor {v}')

