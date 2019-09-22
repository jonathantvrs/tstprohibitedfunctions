# -*- coding: utf-8  -*-
# author: jonathan.tavares.silva
# matricula: 118210631
nota_um = float(raw_input())
nota_dois = float(raw_input())
nota_tres = float(raw_input())
peso_um = float(raw_input())
peso_dois = float(raw_input())

peso_tres = 100 - (peso_um + peso_dois)
media_final = (nota_um * peso_um + nota_dois * peso_dois + nota_tres * peso_tres) / 100

print "Média Final: %.1f" % media_final
