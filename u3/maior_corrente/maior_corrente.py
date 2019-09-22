# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

tensao_um = int(raw_input())
resistencia_um = int(raw_input())
tensao_dois = int(raw_input())
resistencia_dois = int(raw_input())
tensao_tres = int(raw_input())
resistencia_tres = int(raw_input())

corrente_um = tensao_um / float(resistencia_um)
corrente_dois = tensao_dois / float(resistencia_dois)
corrente_tres = tensao_tres / float(resistencia_tres)

if corrente_um > corrente_dois and corrente_um > corrente_tres:
    if corrente_um < (10 ** -3):
        corrente_um *= 10 ** 6 
        simbolo = 'µA'       
    elif 10 ** -3 <= corrente_um < 1:
        corrente_um *= 10 ** 3   
        simbolo = 'mA'
    else:
        simbolo = 'A'       

    print "condutor com maior corrente: 1"
    print "maior corrente: %.2f %s" % (corrente_um, simbolo)
elif corrente_dois > corrente_um and corrente_dois > corrente_tres:
    if corrente_dois < 10 ** -3:
        corrente_dois *= 10 ** 6
        simbolo = 'µA'        
    elif 10 ** -3 <= corrente_dois < 1:
        corrente_dois *= 10 ** 3
        simbolo = 'mA'
    else:
        simbolo = 'A'   
    print "condutor com maior corrente: 2"
    print "maior corrente: %.2f %s" % (corrente_dois, simbolo)
elif corrente_tres > corrente_um and corrente_tres > corrente_dois:
    if corrente_tres < 10 ** -3:
        corrente_tres *= 10 ** 6
        simbolo = 'µA'        
    elif 10 ** -3 <= corrente_tres < 1:
        corrente_tres *= 10 ** 3
        simbolo = 'mA'
    else:
        simbolo = 'A'   
    print "condutor com maior corrente: 3"
    print "maior corrente: %.2f %s" % (corrente_tres, simbolo)

