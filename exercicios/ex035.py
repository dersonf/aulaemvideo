#!/usr/bin/python36
print('\033[1;32m-=\033[m' * 20)
print('Analisador de Triângilos')
print('\033[1;32m-=\033[m' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < (b + c) and a > (b - c):
    triangulo = ('\033[1;32;44mPODEM FORMAR\033[m')
else:
    triangulo = ('\033[1;31;44mNÃO PODEM FORMAR\033[m')
print('Os segmentos acima {} triângulo!'.format(triangulo))
