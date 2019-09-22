# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero = int(raw_input())

fatorial = 1
for i in range(numero, 0, -1):
    fatorial *= i

print fatorial
