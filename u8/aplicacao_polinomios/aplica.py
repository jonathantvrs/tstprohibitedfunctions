# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

while True:
    entrada = raw_input().split()    
    if entrada[0] != "fim": 
        if entrada[0] == "p:":
            polinomio = []
            print "novo polinomio"
            for i in range(len(entrada) - 1, 0, -1):
                polinomio.append(int(entrada[i]))
        else:
            valor_polinomio = 0
            for i in range(len(polinomio) - 1, -1, -1):
                valor_polinomio += polinomio[i] * int(entrada[0]) ** (len(polinomio) - i - 1) 
        
            print valor_polinomio 
    else:
        break
