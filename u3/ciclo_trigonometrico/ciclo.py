# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

angulo = float(raw_input())

if angulo > 360:
    angulo = angulo % 360
    if 0 < angulo < 90:
        print "Quadrante 1"
    elif 91 <= angulo < 180:
        print "Quadrante 2"
    elif 181 <= angulo < 270:
        print "Quadrante 3"
    elif 271 <= angulo < 360:
        print "Quadrante 4"
    elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
        print "Sobre eixos"
else:
     if 0 < angulo < 90:
        print "Quadrante 1"
     elif 91 <= angulo < 180:
        print "Quadrante 2"
     elif 181 <= angulo < 270:
        print "Quadrante 3"
     elif 271 <= angulo < 360:
        print "Quadrante 4"
     elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
        print "Sobre eixos"
