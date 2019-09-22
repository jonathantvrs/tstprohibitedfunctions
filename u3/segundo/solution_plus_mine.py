# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

sequence = ""

n1 = int(raw_input())
n2 = int(raw_input())

sequence += str(n1) + ", " + str(n2) + ", "

if n2 > n1:
    n2, n1 = n1, n2

n3 = int(raw_input())

sequence += str(n3) + " e "

if n3 > n2:
    n3, n2 = n2, n3
    if n2 > n1:
        n2, n1 = n1, n2

n4 = int(raw_input())

sequence += str(n4)

if n4 > n3:
    n4, n3 = n3, n4
    if n3 > n2:
        n3, n2 = n2, n3
        if n2 > n1:
            n2, n1 = n1, n2

print "Considerando os números " + sequence
print "O segundo menor número é %d" % n3
print "O segundo maior número é %d" % n2
