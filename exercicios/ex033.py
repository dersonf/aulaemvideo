#!/usr/bin/python36
pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
tv = int(input('Terceiro valor: '))
if pv < sv and pv < tv:
    menorvalor = pv
if sv < pv and sv < pv:
    menorvalor = sv
if tv < pv and tv < sv:
    menorvalor = tv
print('O menor valor digitado é {}'.format(menorvalor))
if pv > sv and pv > tv:
    mv = pv
if sv > pv and sv > tv:
    mv = sv
if tv > pv and tv > sv:
    mv = tv
print('O maior valor digitado é {}'.format(mv))
