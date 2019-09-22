# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

dia_da_semana = raw_input()
quantidade_de_clientes = int(raw_input())

if dia_da_semana != "sábado" and dia_da_semana != "domingo":
    if 40 <= quantidade_de_clientes <= 60:
        print "normal"
    else:
        print "atípico"
else:
    if quantidade_de_clientes >= 40:
        print "normal"
    else:
        print "atípico"
    
