# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero_um = int(raw_input())
numero_dois = int(raw_input())
numero_tres = int(raw_input())

aposta_um = numero_um % 11
aposta_dois = numero_dois % 11
aposta_tres = numero_tres % 11

print "%.2d-%.2d-%.2d" % (aposta_um, aposta_dois, aposta_tres)
