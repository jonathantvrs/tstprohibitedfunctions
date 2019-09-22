# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def agrupa_multiplos(seq, k):
    for i in range(len(seq) - 1):
        for j in range(len(seq) - 1):
            if seq[j] % k != 0 and seq[j + 1] % k == 0:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]

a = [6,15,12,6,8,3,25,14,1,10,7]
agrupa_multiplos(a, 5)

print a
