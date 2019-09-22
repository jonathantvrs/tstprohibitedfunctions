# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

cre = float(raw_input())
experience = int(raw_input())
interview = int(raw_input())

if cre < 7 and experience < 6:
    print "Candidato eliminado. CRE e experiência abaixo do limite."
elif cre >= 7 and experience >= 6:
    if interview <= 3:
        print "Candidato classificado."
    else:
        print "Candidato aprovado."

if cre < 7 and experience >= 6: 
    print "Candidato eliminado. CRE abaixo do limite."
elif cre >= 7 and experience < 6:
    print "Candidato eliminado. Experiência abaixo do limite."


