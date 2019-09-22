# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero_criterio = int(raw_input())

conta_numeros_maiores, numero_sequencia = 0, 0
while True:
    sequencia = raw_input()
    lista_sequencia = sequencia.split()
    numero_sequencia += 1
    
    if sequencia != "fim":
        for i in range(len(lista_sequencia)):
            if int(lista_sequencia[i]) > numero_criterio:
                conta_numeros_maiores += 1
        
        if conta_numeros_maiores > (len(lista_sequencia) / 2):
            print "sequencia %d: %s" % (numero_sequencia, sequencia)
        
        conta_numeros_maiores = 0
    else: 
        break
