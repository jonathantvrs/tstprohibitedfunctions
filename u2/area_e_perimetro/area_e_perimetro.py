# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

import math

diametro = int(raw_input())

raio = diametro / 2.0
area  = math.pi * raio ** 2.0
perimetro = 2.0 * math.pi * raio

print "A: %.5f" %  area
print "P: %.5f" % perimetro
