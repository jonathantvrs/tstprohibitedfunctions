# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero_um = int(raw_input())
numero_dois = int(raw_input())
numero_tres = int(raw_input())

soma = numero_um + numero_dois + numero_tres

if soma % 3 == 0 and soma % 5 == 0:
    print "plifplof"
elif soma % 3 == 0:
    print "plif"
elif soma % 5 == 0:
    print "plof"
else:
    print soma
