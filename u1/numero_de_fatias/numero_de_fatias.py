# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

convidados = int(raw_input())

print "Opção 1: %d fatias cada, %d de resto" % ((32 / convidados), (32 % convidados))
print "Opção 2: %.2f fatias cada" % (32.0 / convidados)
