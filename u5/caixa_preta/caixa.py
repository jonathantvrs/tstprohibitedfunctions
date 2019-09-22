# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

contador_peso, contador_combustivel, contador_altitude = 0, 0, 0
while True:
    caixa = raw_input().split()
 
    peso, combustivel, altitude = int(caixa[0]), int(caixa[1]), int(caixa[2])
    
    if peso >= 0:
        contador_peso += 1
    else:
        print "dado inconsistente. peso negativo."
        break 
   
    if combustivel >= 0:
        contador_combustivel += 1 
    else:
        print "dado inconsistente. combustível negativo."
        break 
    
    if altitude >= 0: 
        contador_altitude += 1
    else:
        print "dado inconsistente. altitude negativa."
        break
   
   
    
print "peso: %d" % contador_peso
print "combustível: %d" % contador_combustivel
print "altitude: %d" % contador_altitude
