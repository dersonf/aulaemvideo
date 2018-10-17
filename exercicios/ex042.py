#!/usr/bin/python36
print('\033[1;32m-=\033[m' * 20)
print('Analisador de Triângilos')
print('\033[1;32m-=\033[m' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
'''if a < (b + c) and a > (b - c):
    print('Os segmentos acima '\033[1;32;44mPODEM FORMAR\033[m um triângulo')
#    if a == b == c:
#        print('Este triângulo é EQUILÁTERO')
#    elif a == b != c or a == c != b or b == c != a:
#        print('Este triângulo é ISÓSCELES')
#    else:
#        print('Este triângulo é ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')'''
#if a < (b + c) and a > (b - c):
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a == b != c or a == c != b or b == c != a:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os seguimentos acima NÂO PODEM formar um triângulo.')
