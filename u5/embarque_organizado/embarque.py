# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

poltronas = raw_input().split()


posicao, par_antes_impar = 0, False 
while posicao < len(poltronas) - 1:
    if int(poltronas[posicao]) % 2 == 0 and int(poltronas[posicao + 1]) % 2 != 0:
        print "erro"
        par_antes_impar = True
    posicao += 1

if not par_antes_impar:
    print "ok"
