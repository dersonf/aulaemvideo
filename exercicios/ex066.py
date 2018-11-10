#!/usr/bin/python36
s = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    else:
        s += n
        c += 1
print(f'Foram digitados {c} número(s) e a soma é {s}.')
 
