# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
print "== Estágio 1 =="

peso_um = float(raw_input("Peso? "))
nota_um = float(raw_input("Nota? "))

print "== Estágio 2 =="

peso_dois = float(raw_input("Peso? "))
nota_dois = float(raw_input("Nota? "))

print "== Estágio 3 =="

peso_tres = float(raw_input("Peso? "))
nota_tres = float(raw_input("Nota? "))

media_parcial = peso_um * nota_um + peso_dois * nota_dois + peso_tres * nota_tres

nota_media_cinco = (media_parcial * 0.6 - 5.0) / 0.4
nota_media_sete = (media_parcial * 0.6 - 7.0) / 0.4

print "== Resultados =="
print "Média parcial: %.1f" % media_parcial
print "Nota na final, pra média 5.0 = %.1f" % abs(nota_media_cinco)
print "Nota na final, pra média 7.0 = %.1f" % abs(nota_media_sete)
