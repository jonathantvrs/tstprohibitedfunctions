# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

for numero in range(1, 102, 2):
    if numero % 3 == 0 or numero % 5 == 0:
        print "*"
    else:
        print numero
