# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

number = int(raw_input())
int_sequence = raw_input().split()

it_is = False
for i in range(len(int_sequence)):
    if number == int(int_sequence[i]):
        print "sim"
        it_is = True
        break

if not it_is:
    print "não"

