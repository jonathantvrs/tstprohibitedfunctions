# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

nota_um = float(raw_input())
nota_dois = float(raw_input())
nota_tres = float(raw_input())
numero_faltas = int(raw_input())

media = (nota_um + nota_dois + nota_tres) / 3

if numero_faltas < 8:
    if media >= 7:
        print "aprovado por media"
    elif 4 <= media < 7:
        print "prova final"
    else: 
        print "reprovado por nota"
else:
    print "reprovado por faltas"
