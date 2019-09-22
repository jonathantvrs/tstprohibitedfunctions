# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

ax = int(raw_input())
ay = int(raw_input())
bx = int(raw_input())  
by = int(raw_input())
cx = int(raw_input())
cy = int(raw_input())

distancia_a_b = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2) 
distancia_a_c = math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
distancia_b_c = math.sqrt((cx - bx) ** 2 + (cy - by) ** 2)

perimetro_triangulo = distancia_a_b + distancia_a_c + distancia_b_c
 
print "O perímetro é de %.2f" % perimetro_triangulo
