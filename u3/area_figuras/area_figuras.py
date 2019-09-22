# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
from math import pi

tipo_figura = raw_input()

if tipo_figura == 'círculo':
    raio = float(raw_input())
    
    print "Área do círculo: %.2f (cm2)" % (pi * raio ** 2)
elif tipo_figura == 'quadrado':
    lado = float(raw_input())
    
    print "Área do quadrado: %.2f (cm2)" % (lado ** 2)
elif tipo_figura == 'triângulo':
    base = float(raw_input())
    altura = float(raw_input())

    print "Área do triângulo: %.2f (cm2)" % (base * altura / 2)
elif tipo_figura == 'retângulo':
    base = float(raw_input())
    altura = float(raw_input())

    print "Área do retângulo: %.2f (cm2)" % (base * altura)
else:
    print "Digite uma figura correta"
