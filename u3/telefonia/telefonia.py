# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

minutos_ligacao = int(raw_input())

valor_total = 1.00

if minutos_ligacao == 1:
    valor_total += 0.50
elif minutos_ligacao == 2:
    valor_total += 1.00
elif minutos_ligacao == 3:
    valor_total += 1.50
elif minutos_ligacao > 3:
    if minutos_ligacao % 5 == 0:
        valor_total += ((minutos_ligacao / 5) * 3.00)
    else:
        valor_total += ((minutos_ligacao / 5) * 3.00) + ((minutos_ligacao % 5) * 0.70)
print "R$ %.2f" % valor_total 
