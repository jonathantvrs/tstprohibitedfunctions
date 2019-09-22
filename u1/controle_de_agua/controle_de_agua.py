# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

velocidade_de_vazao = float(raw_input())
diametro_do_cano = float(raw_input())
tempo = int(raw_input())

seccao = (math.pi * diametro_do_cano ** 2) / 4
vazao = velocidade_de_vazao * seccao * 1000
quantidade_de_agua = tempo * vazao

print "Quantidade de água =", quantidade_de_agua, "litros."
