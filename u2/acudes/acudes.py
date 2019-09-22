# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

capacidade_total = float(raw_input("capacidade? "))
percentual_hoje = float(raw_input("percentual hoje? "))
gasto_diario = float(raw_input("gasto diário? "))

volume = capacidade_total * (percentual_hoje / 100)
dias_restantes = volume / gasto_diario

print "volume: %.2f" % volume
print "dias restantes: %d" % dias_restantes
