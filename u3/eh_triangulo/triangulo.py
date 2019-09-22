# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

exp_um = abs(b - c) < a < b + c
exp_dois = abs(a - c) < b < a + c
exp_tres = abs(a - b) < c < a + b

if exp_um and exp_dois and exp_tres:
    print "triangulo valido. %d" % (a + b + c)
else:
    print "triangulo invalido." 

