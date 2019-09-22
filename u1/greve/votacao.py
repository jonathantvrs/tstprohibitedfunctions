# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
votos_abstencao = int(raw_input())
votos_favor = int(raw_input())
votos_contra = int(raw_input())

total_votos = float(votos_abstencao + votos_favor + votos_contra)

percentual_abstencao = votos_abstencao / total_votos * 100
percentual_favor = votos_favor / total_votos * 100
percentual_contra = votos_contra / total_votos * 100

print "Resultado da Votação"
print
print "%d abstenções (%.2f%%)" % (votos_abstencao, percentual_abstencao)
print "%d a favor (%.2f%%)" % (votos_favor, percentual_favor)
print "%d contra (%.2f%%)" % (votos_contra, percentual_contra)
