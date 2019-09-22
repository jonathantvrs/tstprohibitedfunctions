# -*- coding: utf-8 -*- 
# author: jonathan.tavares.silva
# matricula: 118210631
adultos = int(raw_input())
criancas = int(raw_input())
preco_ingresso = float(raw_input())

total = preco_ingresso * adultos + preco_ingresso / 2 * criancas

print "Total: R$ " + str(total)
