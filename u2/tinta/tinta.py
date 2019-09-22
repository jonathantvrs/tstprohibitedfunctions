# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

altura_parede = float(raw_input())
largura_parede = float(raw_input())

litros_tinta = (altura_parede * largura_parede) / 50 * 3.6

print "%.2f l" % litros_tinta
