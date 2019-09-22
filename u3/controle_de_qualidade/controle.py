# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

peso_antes = float(raw_input())
peso_depois = float(raw_input())

percentagem_agua = (peso_antes - peso_depois) / peso_antes * 100.0

print "%.1f%% do peso do produto é de água congelada." % percentagem_agua

if percentagem_agua >= 10:
    print "Produto não conforme."
elif percentagem_agua < 5:
    print "Produto qualis A."
else:
    print "Produto em conformidade." 
