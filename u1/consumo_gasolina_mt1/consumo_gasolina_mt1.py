# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
pos_inicial = float(raw_input())
litros_inicial = float(raw_input())
pos_final = float(raw_input())
litros_final = float(raw_input())

consumo = abs((pos_final - pos_inicial) / (litros_final - litros_inicial))

print "%.1f" % consumo
