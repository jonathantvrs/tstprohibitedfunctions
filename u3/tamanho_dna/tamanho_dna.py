# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

dna_um = raw_input()
dna_dois = raw_input()
dna_tres = raw_input()

sequencia_um, sequencia_dois, sequencia_tres = len(dna_um), len(dna_dois), len(dna_tres) 
menor = " "


if sequencia_um < sequencia_dois and sequencia_um < sequencia_tres:
    menor = dna_um
elif sequencia_dois < sequencia_um and sequencia_dois < sequencia_tres:
    menor = dna_dois
elif sequencia_tres < sequencia_um and sequencia_tres < sequencia_dois:
    menor = dna_tres
elif sequencia_um == sequencia_dois:
    menor = dna_um
elif sequencia_dois == sequencia_tres:
    menor = dna_dois
elif sequencia_um == sequencia_tres:
    menor = dna_um

print "%s %d" % (menor, len(menor))
