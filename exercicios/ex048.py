#!/usr/bin/python36
s = 0
v = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        s += c
        v += 1
print('A soma dos {} valores é {}'.format(v, s))

