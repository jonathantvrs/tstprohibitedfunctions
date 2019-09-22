# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

tipo_produto = raw_input()
area_pulverizada = int(raw_input())

if tipo_produto == "Fungicida":
    quantidade_produto = math.ceil(area_pulverizada / 50.0)
    preco_produto = quantidade_produto * 320.0
elif tipo_produto == "Herbicida":
    quantidade_produto = math.ceil(0.3 * area_pulverizada / 1.0)
    preco_produto = quantidade_produto * 100.0
elif tipo_produto == "Inseticida":
    quantidade_produto = math.ceil(2.5 * area_pulverizada / 30.0)
    preco_produto = quantidade_produto * 400.0

print "%d %s(s). %.2f reais." % (quantidade_produto, tipo_produto, preco_produto)
