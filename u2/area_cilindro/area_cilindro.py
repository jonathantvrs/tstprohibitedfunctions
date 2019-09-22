# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

print "Cálculo da Superfície de um Cilindro\n---"

diametro_cilindro = float(raw_input("Medida do diâmetro? "))
altura_cilindro = float(raw_input("Medida da altura? "))

raio = diametro_cilindro / 2
area_cilindro = 2 * raio * altura_cilindro * math.pi + 2 * math.pi * raio ** 2

print "---\nÁrea calculada: %.2f" % area_cilindro
