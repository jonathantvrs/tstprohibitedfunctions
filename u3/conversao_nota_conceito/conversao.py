# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

nota_um = float(raw_input())
nota_dois = float(raw_input())
nota_tres = float(raw_input())
nota_quatro = float(raw_input())

media_anual = (nota_um + nota_dois + nota_tres + nota_quatro) / 4.0

if media_anual < 4:
    print "Conceito E."
elif 4 <= media_anual < 6:
    print "Conceito D."
elif 6 <= media_anual < 7.5:
    print "Conceito C."
elif 7.5 <= media_anual < 9:
    print "Conceito B."
else:
    print "Conceito A."
