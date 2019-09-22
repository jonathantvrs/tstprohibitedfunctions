# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

quantidade_km = float(raw_input())
tempo = float(raw_input())

velocidade = quantidade_km / tempo

if velocidade < 10:
    corredor = 'amador'
elif 10 <= velocidade <= 15:
    corredor = 'aspirante'
else:
    corredor = 'profissional'


print "Velocidade: %.1fkm/h. Corredor %s." % (velocidade, corredor)
