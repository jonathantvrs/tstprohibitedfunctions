# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

dado = raw_input()

conta_elementos, numero_conjunto, mais_elementos = 0, 0, 0
while dado != "fim":
    if int(dado) < 0:
        numero_conjunto += 1
        if conta_elementos > mais_elementos:
            mais_elementos = conta_elementos
            # conta_elementos = 0
        elif conta_elementos == mais_elementos:
            numero_conjunto = 1
        conta_elementos = 0       
    else:
        conta_elementos += 1

    dado = raw_input()

if numero_conjunto > 0:
    print "Conjunto %d - %d elemento(s)" % (numero_conjunto, mais_elementos)    
