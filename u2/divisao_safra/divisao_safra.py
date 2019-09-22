# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

quantidade_de_soja = int(raw_input())
quantidade_clientes_atacado = int(raw_input())
quantidade_clientes_varejo = int(raw_input())

quantidade_atacado = quantidade_de_soja / quantidade_clientes_atacado
quantidade_varejo = float(quantidade_de_soja) % quantidade_clientes_atacado / quantidade_clientes_varejo

print "Clientes no atacado = %dkg cada." % quantidade_atacado
print "Clientes no varejo = %.2fkg cada." % quantidade_varejo 
