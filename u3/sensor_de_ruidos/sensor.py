# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

ruido = raw_input()
hora = int(raw_input())

if ruido == "":
    print "Condomínio em Paz."
else:
    if 22 <= hora <= 24 or hora <= 6:
        print "Perturbação Detectada!"
    else:
        print "Condomínio em Paz."
