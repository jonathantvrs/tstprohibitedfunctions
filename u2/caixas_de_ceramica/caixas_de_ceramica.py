# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

capacidade_de_revestimento = float(raw_input("Capacidade de revestimento? "))

print "\n== Dados do vão a revestir =="

comprimento_do_vao = float(raw_input("Comprimento? "))
largura_do_vao = float(raw_input("Largura? "))
altura_do_vao = float(raw_input("Altura? "))

area_total = (altura_do_vao * comprimento_do_vao) * 4 + largura_do_vao * comprimento_do_vao
numero_de_caixas = area_total / capacidade_de_revestimento

print "\n== Resultados =="
print "Área total a revestir: %.1f m2" % area_total
print "Número de caixas: %d" % numero_de_caixas
