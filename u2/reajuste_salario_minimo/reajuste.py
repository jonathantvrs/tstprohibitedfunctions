# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

valor_atual = float(raw_input("Valor atual? "))
novo_valor = float(raw_input("Novo valor? "))

reajuste = (novo_valor - valor_atual) * 100.0 / valor_atual 

print "Reajuste de %.1f%%" % reajuste
