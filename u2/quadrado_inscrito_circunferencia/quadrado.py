# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

lado_quadrado = float(raw_input())

perimetro = 2.0 * math.pi * (lado_quadrado * math.sqrt(2) / 2)
area_interna = math.pi * ((lado_quadrado * math.sqrt(2) / 2) ** 2) 

print "Perímetro: %.5f" % perimetro
print "Área: %.5f" % area_interna
