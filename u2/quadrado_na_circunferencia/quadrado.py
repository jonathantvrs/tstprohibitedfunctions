# -*- coding: utf-8
# author: jonathan.tavares.silva
# matricula: 118210631
from math import pi, sqrt

raio = float(raw_input())

area_circunferencia = pi * raio ** 2
area_quadrado = (raio * 2 / sqrt(2)) ** 2 
area_nao_comum = area_circunferencia - area_quadrado

print "Área não comum: %.5f" % area_nao_comum 
