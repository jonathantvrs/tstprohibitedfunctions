# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())


delta = b ** 2 - 4 * a * c

if a != 0:
    if delta < 0:
        print "sem raizes reais"
    elif delta == 0:
        x = (-b) / (2.0 * a)
        print "x = %.2f" % x
    else:
        x1 = ((-b) + math.sqrt(delta)) / (2.0 * a)
        x2 = ((-b) - math.sqrt(delta)) / (2.0 * a)
        print "x1 = %.2f" % x1
        print "x2 = %.2f" % x2
