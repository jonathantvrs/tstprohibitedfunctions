# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

cateto_one = float(raw_input("Medida do Cateto 1? "))
cateto_two = float(raw_input("Medida do Cateto 2? "))

print "Medida da Hipotenusa: %.2f" % (math.sqrt(cateto_one ** 2 + cateto_two ** 2))
