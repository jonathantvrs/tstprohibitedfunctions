# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

distancia_aeroportos = float(raw_input())
aliquota = float(raw_input())

valor_passagem = distancia_aeroportos * aliquota + 51
passagem_a_vista = valor_passagem - (valor_passagem * 0.25)
passagem_seis_parcelas = valor_passagem - (valor_passagem * 0.05)

print "Valor da passagem: R$ %.2f" % valor_passagem
print ""
print "Pagamento:"
print "1. À vista. R$ %.2f" % passagem_a_vista
print "2. Em 6 parcelas. Total: R$ %.2f" % passagem_seis_parcelas
print "   6 x R$ %.2f" % (passagem_seis_parcelas / 6.0)
print "3. Em 10 parcelas. Total: R$ %.2f" % valor_passagem
print "   10 x R$ %.2f" % (valor_passagem / 10.0)
