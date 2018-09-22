#!/usr/bin/python36
nome = str(input('Digite seu nome completo: ')).strip()
#nome = nome.strip() adicionado já no input
lista = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo {} letras'.format(len(nome.replace(' ',''))))
#print('Seu nome ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(lista[0], len(lista[0])))
