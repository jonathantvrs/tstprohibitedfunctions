# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

area_construida_casa = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))

iptu = area_construida_casa * aliquota + 35
iptu_quota_unica = iptu - (iptu * 0.25)
iptu_seis_parcelas = iptu - (iptu * 0.05)

print "IPTU: R$ %.2f" % iptu
print ""
print "Pagamento:"
print "1. Quota única. R$ %.2f" % iptu_quota_unica
print "2. Em 6 parcelas. Total: R$ %.2f" % iptu_seis_parcelas
print "   6 x R$ %.2f" % (iptu_seis_parcelas / 6.0)
print "3. Em 10 parcelas. Total: R$ %.2f" % iptu
print "   10 x R$ %.2f" % (iptu / 10.0)
