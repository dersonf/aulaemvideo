#!/usr/bin/python36
palavras = ('mercado', 'curso', 'oportunidade', 'mensalidade', 'gabriel',
    'gasolina', 'alcool', 'bombocado')
for c in palavras:
    print(f'Na palavra {c.upper()} tem as vogais', end = ' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
    print()

