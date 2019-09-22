# -*- coding: utf-8  -*-
# author: jonathan.tavares.silva
# matricula: 118210631
posicao_inicial = float(raw_input())
velocidade = float(raw_input())
tempo = float(raw_input())

print "Posição final do móvel"
print "S(%.1f) = %.1f m" % (tempo, (posicao_inicial + velocidade * tempo))
