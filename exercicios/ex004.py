#!/usr/bin/python36
# Desafio 04 da Aula 06

a = input('Digite algo: ') # Esse a é um objeto, ele possui atributos e valores.
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?',a.isspace())
print('Só tem números?',a.isnumeric())
print('Só tem letras?',a.isalpha())
print('É alfanumérico, possui letras e/ou números?',a.isalnum())
print('Toda em maiúsculas?',a.isupper())
print('Toda em minúscula?',a.islower())
print('Está capitalizada, possui letra maiúsculas e minúsculas?',a.istitle())
print()
print('Essa bixiga só tem letras? {}'.format(a.isalpha()))
print('Essa bixiga é numérica? {}'.format(a.isnumeric()))
