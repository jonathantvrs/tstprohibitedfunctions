# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

conta = int(raw_input())

primeiro_digito = conta / 10000 % 10
segundo_digito = conta / 1000 % 10
terceiro_digito = conta / 100 % 10
quarto_digito = conta / 10 % 10
quinto_digito = conta / 1 % 10
 
digito_verificador = (primeiro_digito + segundo_digito + terceiro_digito + quarto_digito + quinto_digito) % 11

print "%.5d-%.2d" % (conta, digito_verificador)
