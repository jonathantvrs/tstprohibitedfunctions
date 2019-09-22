# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

agenda = []

while True:
    nome = raw_input()

    if nome != "####":
        agenda.append(nome)
        
        for j in range(len(agenda)):
            for i in range(len(agenda) - 1):
                if agenda[i] > agenda[i + 1]:
                    agenda[i], agenda[i + 1] = agenda[i + 1], agenda[i]
        for element in agenda:
            if element == nome:
                print "* %s" % element
            else:
                print element
        print "----"    
    else: 
        break        
