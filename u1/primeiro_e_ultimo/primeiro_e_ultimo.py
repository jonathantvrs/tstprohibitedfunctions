# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
numero = int(raw_input())

primeiro_digito = numero / 1000 % 10 
ultimo_digito = numero / 1 % 10

print "%d %d" % (primeiro_digito, ultimo_digito)
