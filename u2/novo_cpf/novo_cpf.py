# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

primeira_parte = int(raw_input())
segunda_parte = int(raw_input())
terceira_parte = int(raw_input())

digito_um = terceira_parte / 100 % 10
digito_dois = terceira_parte / 10 % 10
digito_tres = terceira_parte / 1 % 10

quarta_parte = digito_um + digito_dois + digito_tres

print "%.3d.%.3d.%.3d-%.2d" % (primeira_parte, segunda_parte, terceira_parte, quarta_parte)    
