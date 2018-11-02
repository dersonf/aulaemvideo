#!/usr/bin/python36
print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)
a1 = 0
a2 = 0
s = 0
c = t = int(input('Quantas termos você quer mostrar? '))
while c != 0:
    print(s,end=' - ')
    if t == c:
        s = a1 = 1
        c = c-1
    elif t-1 == c:
        s = a2 = 1
        c = c-1
    else:
        s = a1 + a2
        a1 = a2
        a2 = s
        c = c-1
print('FIM')

