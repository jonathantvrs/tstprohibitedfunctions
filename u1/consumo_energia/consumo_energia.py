# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

potencia_equipamento = int(raw_input())
tempo_ligado = int(raw_input())

consumo = (potencia_equipamento / 1000.0) * (tempo_ligado / 60.0)

print str(consumo) + " kWh"
