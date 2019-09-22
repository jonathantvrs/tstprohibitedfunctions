# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

peso_perder = float(raw_input())
tempo_exercicios = float(raw_input())
consumo_calorias = float(raw_input())

quantidade_calorias_perder = peso_perder * 7700
quantidade_calorias_exercicio = tempo_exercicios * 900

quantidade_dias = (quantidade_calorias_perder / (quantidade_calorias_exercicio + 2000 - consumo_calorias)) 

print "Você precisará de %.2f dias de dieta" % quantidade_dias
