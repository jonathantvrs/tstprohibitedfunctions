# -*- coding:utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

altura_arvore = int(raw_input())

for i in range(altura_arvore):
	print " " * (altura_arvore - i - 1) + "o" * (2 * i + 1)

print " " * (altura_arvore - 1) + "o"
