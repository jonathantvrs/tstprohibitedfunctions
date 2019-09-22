# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

tempo_disponivel = int(raw_input())
quantidade_de_avioes = int(raw_input())

voos_autorizados = 0

for aviao in range(quantidade_de_avioes):
    tempo_aviao = int(raw_input())
    if (tempo_disponivel - tempo_aviao) >= 0:
        tempo_disponivel -= tempo_aviao 
    
        if tempo_disponivel >= 0:
            voos_autorizados += 1

print "%d voo(s) autorizados." % voos_autorizados
