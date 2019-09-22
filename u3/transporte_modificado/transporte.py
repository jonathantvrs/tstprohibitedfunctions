# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

numero_pessoas = int(raw_input())
valor_disponivel = float(raw_input())

preco_tav = 100.00 * numero_pessoas
preco_onibus = 22.00 * numero_pessoas
preco_taxi = math.floor(valor_disponivel / 200) * 200


if valor_disponivel >= preco_tav:
    print "TAV. R$ %.2f" % preco_tav
elif (preco_taxi / numero_pessoas) > 49:
    print "Táxi. R$ %.2f" % preco_taxi
elif valor_disponivel >= preco_onibus:
    print "Ônibus. R$ %.2f" % preco_onibus
else:
    print "Não é possível realizar a viagem."
