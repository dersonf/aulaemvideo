#!/usr/bin/python36
frase = input('Digite uma frase: ').upper().strip().replace(' ','')
invert = frase[::-1]
print('O inverso de {} é {}'.format(frase, invert))
if invert == frase:
    print('Temos um palíndromo!')
else:
    print('Não temos um palídromo')

