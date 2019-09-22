# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

lado_um = float(raw_input())
lado_dois = float(raw_input())
area_casa = float(raw_input())

area_terreno = lado_um * lado_dois
quantidade_casas_terreno = area_terreno / area_casa

print "%d casa(s) pode(m) ser construída(s) no terreno." % quantidade_casas_terreno
