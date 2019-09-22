# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def busca(seq, v):
    for i in range(len(seq)):
        if seq[i] == v:
            return i
    return -1

seq = [8,9,2,3,6,10,7,9]
print busca(seq, 6)
print busca(seq, 4)
print busca(seq, 9)
